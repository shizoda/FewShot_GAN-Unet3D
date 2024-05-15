import nibabel as nb
import os
import tqdm 

def list_files(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))

data_dirs = ['../data/iSeg-2017-Training', '../data/iSeg-2017-Testing']

output_base_dir = '../data/iSEG'
label_base_dir = '../data/iSEG'

_ = [os.makedirs(dir, exist_ok=True) for dir in [output_base_dir, label_base_dir]]

for data_dir in data_dirs:
    files = list_files(data_dir, "img")

    for file_name in files:
        print("Processing %s" % file_name)
        new_fname = os.path.join(data_dir, file_name)
        img = nb.load(new_fname)

        out_dir = os.path.join(output_base_dir, os.path.basename(data_dir.replace("iSeg-2017-","")))
        if 'T1' in file_name:
            out_dir = os.path.join(out_dir, 'T1')
        elif 'T2' in file_name:
            out_dir = os.path.join(out_dir, 'T2')
        elif file_name.find("label") > -1:
            out_dir = os.path.join(out_dir, 'label')
            out_dir = out_dir.replace("_preprocessed", "")
        else:
            raise ValueError("Unknown file type")
            import pdb; pdb.set_trace()

        os.makedirs(out_dir, exist_ok=True)
        out_file = os.path.join(out_dir, os.path.basename(new_fname).replace('.img', '.nii'))
        nb.save(img, out_file)

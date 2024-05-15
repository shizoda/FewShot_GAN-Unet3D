# https://hub.docker.com/r/nvidia/cuda/tags 
FROM nvidia/cuda:11.0.3-cudnn8-devel-ubuntu20.04

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install torch==1.7.1+cu110 torchvision==0.8.2+cu110 -f https://download.pytorch.org/whl/torch_stable.html

RUN pip3 install tqdm nibabel
RUN pip3 install SimpleITK

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install python3-opencv
RUN pip3 install scikit-learn scikit-image

RUN apt-get update && apt-get -y install git

ENV CUDA_DEVICE_ORDER="PCI_BUS_ID"

# Install Jupyter and set up the configuration for external access
RUN pip3 install notebook

# Create a Jupyter Notebook configuration file
RUN jupyter notebook --generate-config  --config=/jupyter_notebook_config.py


# Modify the Jupyter Notebook configuration file to allow external access
RUN echo "c.NotebookApp.allow_origin = '*'" >> /jupyter_notebook_config.py
RUN echo "c.NotebookApp.ip = '0.0.0.0'" >> /jupyter_notebook_config.py
RUN echo "c.NotebookApp.open_browser = False" >> /jupyter_notebook_config.py
RUN echo "c.NotebookApp.port = 8888" >> /jupyter_notebook_config.py


RUN pip3 install SimpleITK sacred
RUN pip3 install easydict
RUN pip3 install tensorboardX nipype

RUN apt-get update && apt-get -y install dcm2niix

# ants のパッケージインストール
RUN apt-get -y install unzip wget
RUN pip3 install antspyx

RUN wget https://github.com/ANTsX/ANTs/releases/download/v2.5.1/ants-2.5.1-ubuntu-20.04-X64-gcc.zip && \
unzip ants-2.5.1-ubuntu-20.04-X64-gcc.zip && \
cp -r ants-2.5.1/bin/* /usr/local/bin/ && \
cp -r ants-2.5.1/lib/* /usr/local/lib/ && \
rm -rf ants-2.5.1 ants-2.5.1-ubuntu-22.04-X64-gcc.zip


# 環境変数の設定
ENV PATH="/usr/local/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/lib:${LD_LIBRARY_PATH}"


# 確認用のコマンド
RUN N4BiasFieldCorrection --version

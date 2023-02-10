# FROM python:3.8
FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN apt update -y && sudo apt upgrade -y && \
    apt-get install -y wget build-essential checkinstall  libreadline-gplv2-dev  libncursesw5-dev  libssl-dev  libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev && \
    cd /usr/src && \
    sudo wget https://www.python.org/ftp/python/3.8.16/Python-3.8.16.tgz && \
    sudo tar xzf Python-3.8.16.tgz && \
    cd Python-3.8.16 && \
    sudo ./configure --enable-optimizations && \
    sudo make altinstall

RUN pip install rdkit
RUN pip install pandas
RUN pip install numpy
# RUN pip install torch==1.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install torch
RUN pip install FPSim2
RUN pip install tqdm
RUN pip install typing-extensions
RUN pip install typed-argument-parser
RUN pip install tensorboardX
RUN pip install scikit-learn
RUN pip install hyperopt
RUN pip install requests

WORKDIR /repo
COPY . /repo
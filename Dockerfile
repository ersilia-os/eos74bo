FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install pandas

# /root/miniconda3/envs/eos/bin/python
WORKDIR /repo
COPY . /repo

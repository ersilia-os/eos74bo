FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge scikit-learn=1.0.2

RUN pip install rdkit==2022.9.5
RUN pip install numpy==1.21.6
RUN pip install pandas==1.1.5
RUN pip install torch==1.8.0+cpu torchvision==0.9.0+cpu torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install tqdm==4.65
RUN pip install typing-extensions==4.5.0
RUN pip install typed-argument-parser==1.8.0
RUN pip install tensorboardX==2.6
RUN pip install hyperopt==0.2.7

WORKDIR /repo
COPY . /repo

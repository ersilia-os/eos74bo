FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install python=3.8
RUN pip install rdkit
RUN pip install numpy
RUN pip install pandas
RUN pip install torch==1.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install tqdm
RUN pip install typing-extensions
RUN pip install typed-argument-parser
RUN pip install tensorboardX
RUN pip install scikit-learn
RUN pip install hyperopt
RUN pip install requests
RUN pip install FPSim2

WORKDIR /repo
COPY . /repo

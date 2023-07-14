FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit-pypi
RUN pip install pytorch==1.7.0
RUN pip install scipy==1.5.2
RUN conda install seaborn=0.11.0=py_0
RUN pip install tqdm
RUN pip install pyyml
RUN pip install scikit-learn==0.23.2

WORKDIR /repo
COPY ./repo

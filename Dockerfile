FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit-pypi==2022.9.5
RUN conda install -c pytorch pytorch=1.7.0
RUN pip install scipy==1.5.2
RUN conda install seaborn=0.11.0=py_0
RUN pip install tqdm==4.67.1
RUN pip install pyyml==0.0.2
RUN pip install scikit-learn==0.23.2

WORKDIR /repo
COPY . /repo

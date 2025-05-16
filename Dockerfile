FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN conda install -c conda-forge scikit-learn==0.23.2
RUN conda install -c conda-forge scipy==1.5.2
RUN pip install rdkit-pypi==2022.9.5
RUN pip install torch==1.7.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
RUN conda install seaborn
RUN pip install tqdm==4.67.1
RUN pip install pyyml==0.0.2

WORKDIR /repo
COPY . /repo

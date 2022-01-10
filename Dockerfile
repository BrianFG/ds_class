FROM jupyter/scipy-notebook:lab-3.2.5

USER root

WORKDIR /home/ucla

COPY requirements.txt .

RUN pip install -r requirements.txt 

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab","--ip=0.0.0.0","--allow-root"]
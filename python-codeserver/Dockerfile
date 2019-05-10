FROM codercom/code-server

USER root

RUN apt-get install python3.7 -y &&\
    apt-get install python3-pip -y &&\
    pip3 install pipenv &&\
    mkdir /code-data &&\
    mkdir /extensions &&\
    mkdir /projects &&\
    chown -R coder /code-data &&\
    chown -R coder /extensions &&\
    chown -R coder /projects

USER coder



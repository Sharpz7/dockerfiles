FROM codercom/code-server

USER root

RUN apt-get install python3.7 -y &&\
    apt-get install python3-pip -y &&\
    pip3 install pipenv &&\
    mkdir /code-data &&\
    mkdir /extensions &&\
    chown -R coder /code-data &&\
    chown -R coder /extensions &&\
    echo "coder:password" | chpasswd

USER coder



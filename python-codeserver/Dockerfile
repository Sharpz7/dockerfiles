FROM codercom/code-server

USER root

RUN apt-get update

RUN apt-get install -y python3.7 \
    python3-pip &&\
    pip3 install pipenv &&\
    mkdir /code-data &&\
    mkdir /extensions &&\
    chown -R coder /code-data &&\
    chown -R coder /extensions &&\
    echo "coder:password" | chpasswd

USER coder



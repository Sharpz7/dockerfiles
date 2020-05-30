FROM codercom/code-server:3.4.0

USER root

RUN apt-get update

# Make Enviroment
RUN mkdir /code-data &&\
    mkdir /extensions &&\
    chown -R coder /code-data &&\
    chown -R coder /extensions

# C++ install
RUN apt-get install -y gcc

# Golang install
RUN wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz && \
    tar -xvf go1.12.7.linux-amd64.tar.gz && \
    mv go /usr/local
ENV GOROOT /usr/local/go
ENV GOPATH /home/coder/project/go
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH

# Python install
RUN apt-get install -y \
    python3.7 \
    python3-pip &&\
    pip3 install pipenv &&\
    pip3 install flake8

# Docker Install
COPY get-docker.sh .

RUN sh get-docker.sh &&\
    curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose &&\
    chmod +x /usr/local/bin/docker-compose

# zsh and zsh plugins
RUN apt-get install -y zsh &&\
	chsh -s /bin/zsh &&\
    touch /home/coder/.zshrc &&\
    usermod -m -d /home/coder coder

ENV SHELL /usr/bin/zsh

# Other nice things
RUN apt-get install -y neofetch
RUN wget https://github.com/Sharpz7/sharp-ops/releases/download/0.3.0a/linux.tar.gz && \
    tar -C /usr/local/bin/ -zxvf linux.tar.gz && \
    chown coder:coder /usr/local/bin/sharpops && \
    chown coder:coder /usr/local/bin/sharpops-data

# ssh support
COPY config /home/coder/.ssh/config
COPY notes.txt /home/coder/notes.txt
COPY commands.sh /home/coder/commands.sh
COPY ssh+ /home/coder/bin/ssh+

# Create files.
RUN touch /home/coder/.ssh/contabo.ssh &&\
    touch /home/coder/.ssh/github.ssh

RUN chown -R coder:coder /home/coder

USER coder

RUN chmod +x /usr/local/bin/sharpops

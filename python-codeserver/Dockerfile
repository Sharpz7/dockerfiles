FROM codercom/code-server:latest

USER root

RUN apt-get update

# Make Enviroment
RUN mkdir /code-data &&\
    mkdir /extensions &&\
    chown -R coder /code-data &&\
    chown -R coder /extensions

# Python install
RUN apt-get install -y \
    python3.7 \
    python3-pip &&\
    pip3 install pipenv

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
    chown coder:coder /usr/local/bin/sharpops

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


FROM codercom/code-server

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
RUN apt-get install -y \
	zsh \
	&& chsh -s /bin/zsh \
    && touch /home/coder/.zshrc \
    && usermod -m -d /home/coder coder

ENV SHELL /usr/bin/zsh

# Other nice things
RUN apt-get install -y neofetch

USER coder

# ssh support
RUN mkdir /home/coder/.ssh &&\
    touch /home/coder/.ssh/contabo.ssh &&\
    touch /home/coder/.ssh/github.ssh &&\
    chmod 700 /home/coder/.ssh && chmod 600 /home/coder/.ssh/contabo.ssh && chmod 600 /home/coder/.ssh/github.ssh

COPY config /home/coder/.ssh/config
COPY notes.txt /home/coder/notes.txt
COPY commands.sh /home/coder/commands.sh
COPY ssh+ /home/coder/ssh+





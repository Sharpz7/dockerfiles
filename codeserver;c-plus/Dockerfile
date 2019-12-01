FROM codercom/code-server:v2

USER root

RUN apt-get update

# Make Enviroment
RUN mkdir /code-data &&\
    mkdir /extensions &&\
    chown -R coder /code-data &&\
    chown -R coder /extensions

# C++ install
RUN apt-get install -y gcc

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

RUN git config --global user.name "Sharpz7"
RUN git config --global user.email "adam@mcaq.me"

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
    && usermod -m -d /home/coder coder \
    && sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" \
    && sed -i -e 's/ZSH_THEME="robbyrussell"/ZSH_THEME="gnzh"/g' ~/.zshrc

ENV SHELL /usr/bin/zsh

# Other nice things
RUN apt-get install -y neofetch

USER coder

# ssh support
RUN mkdir /home/coder/.ssh &&\
    touch /home/coder/.ssh/authorized_keys &&\
    chmod 700 /home/coder/.ssh && chmod 600 /home/coder/.ssh/authorized_keys

COPY config /home/coder/.ssh/config
COPY commands.sh /home/coder/commands.sh





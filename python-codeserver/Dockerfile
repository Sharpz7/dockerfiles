FROM codercom/code-server

USER root

RUN apt-get update

RUN apt-get install -y \
    python3.7 \
    python3-pip &&\
    pip3 install pipenv &&\
    mkdir /code-data &&\
    mkdir /extensions &&\
    chown -R coder /code-data &&\
    chown -R coder /extensions

RUN apt-get install -y \
	zsh \
	&& chsh -s /bin/zsh \
    && touch /home/coder/.zshrc \
    && sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" \
    && usermod -m -d /home/coder coder

ENV SHELL /usr/bin/zsh

USER coder



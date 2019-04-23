FROM codercom/code-server

USER root

RUN apt-get install python3.7 -y
RUN apt-get install python3-pip -y

RUN pip3 install pipenv

RUN mkdir /home/coder/code-data
RUN mkdir /home/coder/extensions

RUN chown -R coder /home/coder/code-data
RUN chown -R coder /home/coder/extensions

USER coder

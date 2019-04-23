FROM codercom/code-server

USER root

RUN apt-get install python3.7 -y
RUN apt-get install python-pip -y

RUN chown -R coder /home/cmder/code-data
RUN chown -R coder /home/cmder/extensions

USER coder

RUN pip install pipenv


FROM codercom/code-server

USER root

RUN apt-get install python3.7 -y
RUN apt-get install python3-pip -y

RUN pip3 install pipenv

RUN mkdir /code-data
RUN mkdir /extensions
RUN mkdir /project

RUN chown -R coder /code-data
RUN chown -R coder /extensions
RUN chown -R coder /project

USER coder

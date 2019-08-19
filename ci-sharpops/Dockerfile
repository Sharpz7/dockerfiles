FROM ubuntu:18.04

RUN apt-get -y update
RUN apt-get install -y wget tar
RUN wget https://github.com/Sharpz7/sharp-ops/releases/download/0.1.0a/linux.tar.gz && \
    tar -C /usr/local/bin/ -zxvf linux.tar.gz && \
    chmod +x /usr/local/bin/sharpops

ENV PATH="/usr/local/bin:${PATH}"

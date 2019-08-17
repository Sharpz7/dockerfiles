FROM golang:1.12

RUN apk add git && \
    mkdir /gopack && \
    wget https://github.com/Sharpz7/gopack/releases/download/0.0.1a/linux.tar.gz && \
    tar -C /gopack -zxvf linux.tar.gz && \
    rm -r linux.tar.gz

ENV PATH="/gopack:${PATH}"
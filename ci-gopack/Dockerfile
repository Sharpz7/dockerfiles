FROM golang:1.12

RUN mkdir /gopack
RUN wget https://github.com/Sharpz7/gopack/releases/download/0.0.1a/linux.tar.gz
RUN tar -C /gopack -zxvf linux.tar.gz
RUN rm -r linux.tar.gz

ENV PATH="/gopack:${PATH}"
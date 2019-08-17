FROM golang:1.12

RUN wget https://github.com/Sharpz7/gopack/releases/download/0.0.1a/linux.tar.gz
RUN tar -C /usr/local/bin/ -zxvf linux.tar.gz
RUN rm -r linux.tar.gz

ENV PATH="/opt/gtk/bin:${PATH}"
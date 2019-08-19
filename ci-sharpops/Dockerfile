FROM bash:latest

RUN apk add ca-certificates
RUN mkdir /bin
RUN wget https://github.com/Sharpz7/sharp-ops/releases/download/0.1.0a/linux.tar.gz && \
    tar -C /bin -zxvf linux.tar.gz && \
    chmod +x /bin/sharpops
    
ENV PATH="/bin:${PATH}"

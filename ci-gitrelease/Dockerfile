FROM golang:1.18-alpine3.16 as builder

RUN apk add git
RUN go get -u github.com/tcnksm/ghr
RUN mkdir /copy
RUN cp ${GOPATH}/bin/ghr /copy/ghr

FROM bash:latest

RUN apk add ca-certificates
COPY --from=builder "/copy/ghr" "/bin/ghr"

ENV PATH="/bin:${PATH}"
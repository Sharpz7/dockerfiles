FROM golang:1.12-alpine3.9 as builder

RUN apk add git
RUN go get -u github.com/tcnksm/ghr
RUN mkdir /copy
RUN cp ${GOPATH}/bin/ghr /copy/ghr

FROM ubuntu:latest

COPY --from=builder "/copy/ghr" "/bin/ghr"

ENV PATH="/bin:${PATH}"
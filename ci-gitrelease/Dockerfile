FROM golang:1.12-alpine3.9 as builder

RUN apk add git
RUN go get -u github.com/tcnksm/ghr

FROM bash:latest

COPY --from=builder "${GOROOT}/bin/ghr" "/ghr/ghr"

ENV PATH="/ghr:${PATH}"
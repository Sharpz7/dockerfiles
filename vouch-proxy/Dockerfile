FROM voucher/vouch-proxy as builder

FROM bash:5

COPY --from=builder / /
COPY config.yml /config/config.yml
COPY setup.sh setup.sh

RUN chmod +x ./setup.sh

CMD [ "./setup.sh", "&&", "/vouch-proxy" ]
FROM voucher/vouch-proxy as builder

FROM bash:5

COPY config.yml /config/config.yml
COPY setup.sh setup.sh
COPY --from=builder / /

RUN chmod +x ./setup.sh

CMD [ "./setup.sh", "&&", "/vouch-proxy" ]
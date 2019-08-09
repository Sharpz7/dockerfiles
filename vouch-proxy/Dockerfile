FROM voucher/vouch-proxy as builder

FROM bash:5

COPY --from=builder / /vouch
COPY config.yml /vouch/config/config.yml

WORKDIR /vouch

COPY setup.sh setup.sh
RUN chmod +x ./setup.sh

CMD [ "./setup.sh" ]
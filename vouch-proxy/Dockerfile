FROM voucher/vouch-proxy as builder

FROM bash:5

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder templates/ templates/
COPY --from=builder /static /static
COPY --from=builder /vouch-proxy /vouch-proxy

COPY setup.sh setup.sh
RUN chmod +x ./setup.sh

CMD [ "./setup.sh" ]
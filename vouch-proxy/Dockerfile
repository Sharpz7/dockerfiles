FROM voucher/vouch-proxy

COPY config.yml /config/config.yml
COPY setup.sh setup.sh

CMD [ "./setup.sh", "&&", "/vouch-proxy" ]
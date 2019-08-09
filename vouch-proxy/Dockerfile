FROM voucher/vouch-proxy

COPY config.yml /config/config.yml
COPY setup.sh setup.sh

RUN chmod +x setup.sh

CMD [ "./setup.sh" ]

ENTRYPOINT ["/vouch-proxy"]
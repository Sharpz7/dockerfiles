FROM nginx:1.15.3

RUN apt-get update -y && \
    apt-get install python3-certbot-nginx -y

CMD ["nginx", "-g", "daemon off;"]
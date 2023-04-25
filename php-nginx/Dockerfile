FROM php:8-fpm-buster

RUN apt update -y && apt install -y nginx

CMD ["sh", "-c", "nginx && php-fpm"]
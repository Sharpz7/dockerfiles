FROM node:8-alpine

RUN apk -U upgrade \
    && apk add git

RUN git clone https://github.com/seejohnrun/haste-server.git /app
WORKDIR /app
RUN npm install
RUN npm install rethinkdbdash

COPY ./app.sh /app/app.sh
RUN chmod 755 app.sh

CMD [ "./app.sh" ]
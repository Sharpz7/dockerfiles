#!/bin/sh

## Add tables to rethink
/usr/local/bin/node ./rethink.js

## run the server
exec /usr/local/bin/node ./server.js
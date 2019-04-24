#!/bin/sh

## Add tables to rethink
exec /usr/local/bin/node ./rethink.js

## run the server
exec /usr/local/bin/node ./server.js
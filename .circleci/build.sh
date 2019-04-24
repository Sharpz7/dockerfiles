#!/bin/sh

arr=(./*)

for ((i=0; i<${#arr[@]}; i++)); do
    if (${arr[$i]} -ne ".circleci") {
        docker pull sharp6292/${arr[$i]}:latest || true
        docker build --cache-from sharp6292/${arr[$i]}:latest -f "${arr[$i]}/Dockerfile" -t sharp6292/${arr[$i]}:latest .
        docker push sharp6292/${arr[$i]}:latest
    }
done
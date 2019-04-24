#!/bin/sh

arr=$(ls ./)

for item in $arr; do
    if ("$item" -ne ".circleci") && ("$item" -ne "README.md"); then
        cd "$item"
        docker pull sharp6292/${item}:latest || true
        docker build --cache-from sharp6292/${item}:latest -f "Dockerfile" -t sharp6292/${item}:latest .
        docker push sharp6292/${item}:latest
        cd ..
    fi
done
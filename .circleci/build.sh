#!/bin/sh

arr=$(ls)

for item in $arr; do
    $dir = $item
    if ("$dir" -ne ".circleci") && ("$dir" -ne "README.md"); then
        cd "$dir"
        docker pull sharp6292/${dir}:latest || true
        docker build --cache-from sharp6292/${dir}:latest -f "Dockerfile" -t sharp6292/${dir}:latest .
        docker push sharp6292/${dir}:latest
        cd ..
    fi
done
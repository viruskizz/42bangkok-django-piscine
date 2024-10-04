#!/bin/sh
URL=$1
if [ -z "$URL" ]; then
    echo "URL not be empty"
    exit 1
fi

curl -s -I "$URL" | grep Location | cut -d ':' -f 2,3 --output-delimiter=':'
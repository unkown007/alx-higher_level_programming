#!/usr/bin/env bash
# Display the body size of HTTP response
#curl -so /dev/null -w '%{size_download}\n' "$1"
curl -sI "$1" | grep 'Content-Length' | sed 's/^Content-Length: //'

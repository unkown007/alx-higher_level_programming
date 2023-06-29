#!/usr/bin/env bash
# Display the size of HTTP response body
curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2

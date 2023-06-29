#!/usr/bin/env bash
# Display the size of HTTP response body
curl -so /dev/null -w '%{size_download}\n' "$1"

#!/bin/bash
# Display the body size of HTTP response
curl -so /dev/null -w '%{size_download}\n' "$1"

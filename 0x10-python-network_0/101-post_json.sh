#!/bin/bash
# sends a JSON POST request to a URL passed as first argument and displays the body of the response
curl -s -X POST -d "@$2" "$1"

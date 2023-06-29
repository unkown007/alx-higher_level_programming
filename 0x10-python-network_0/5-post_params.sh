#!/bin/bash
# Sends a POST request and displays the body of the response
curl -s -X POST -d "test@gmail.com" -d "subject=I+will+always+be+here+for+PLD" "$1"

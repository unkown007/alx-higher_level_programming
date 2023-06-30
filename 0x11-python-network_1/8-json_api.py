#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user wit the letter as a parameter"""
from sys import argv
from requests import post
import json


if __name__ == "__main__":
    if len(argv) == 1:
        par = ''
    else:
        par = argv[1]
    r = post("http://0.0.0.0:5000/search_user", data={'q': par})
    if r.headers.get("content-type") == "application/json":
        if r.text == '{}\n':
            print("No result")
        else:
            data = json.loads(r.text)
            print("[{}] {}".format(data['id'], data['name']))
    else:
        print("Not a valid JSON")

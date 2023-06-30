#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user wit the letter as a parameter"""
from sys import argv
from requests import post, exceptions


if __name__ == "__main__":
    if len(argv) == 1:
        par = ''
    else:
        par = argv[1]
    r = post("http://0.0.0.0:5000/search_user", data={'q': par})
    try:
        data = r.json()
        if len(data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except ValueError as e:
        print("Not a valid JSON")

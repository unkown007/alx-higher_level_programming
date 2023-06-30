#!/usr/bin/python3
""" Sends a POST request to the paassed URL with the email as a parameter
and display the body of the response (decoded in utf-8) """
from sys import argv
from urllib import parse, request


if __name__ == "__main__":
    req = request.Request(
            argv[1],
            data=parse.urlencode({'email': argv[2]}).encode(),
            method="POST")
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))

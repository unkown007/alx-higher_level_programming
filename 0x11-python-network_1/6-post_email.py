#!/usr/bin/python3
""" sends a POST request to the passed URL with the
email as parameter, and finally display the body of the response"""
from sys import argv
from requests import post


if __name__ == "__main__":
    r = post(argv[1], data={'email': argv[2]})
    print(r.text)

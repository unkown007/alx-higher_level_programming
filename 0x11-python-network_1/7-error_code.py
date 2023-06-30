#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """
from sys import argv
from requests import get, exceptions


if __name__ == "__main__":
    try:
        r = get(argv[1])
        r.raise_for_status()
        print(r.text)
    except exceptions.HTTPError as e:
        print("Error code: {}".format(r.status_code))

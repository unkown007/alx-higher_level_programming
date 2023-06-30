#!/usr/bin/python3
""" Sends a request to the URL and display the value of the 
X-request-Id """
from sys import argv
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print("{}".format(response.getheader("X-request-Id")))

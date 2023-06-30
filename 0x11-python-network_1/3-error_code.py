#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response
 (decoded in utf-8) """
from sys import argv
from urllib import request, error


if __name__ == "__main__":
    try:
        response = request.urlopen(argv[1])
        print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))

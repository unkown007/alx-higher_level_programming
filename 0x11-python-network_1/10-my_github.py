#!/usr/bin/python3
""" takes GitHub Credentials and uses GitHub API to display your id """
from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = get(url, auth=(argv[1], argv[2]))
    data = r.json()
    print(data.get('id'))

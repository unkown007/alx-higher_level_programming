#!/usr/bin/python3
""" list 10 commits (from the recent to oldest) of the repo 'rails'
by the user 'rails' """
from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = get(url)
    data = r.json()
    sorted_data = sorted(
            data,
            key=lambda d: d.get('commit').get('author').get('date'),
            reverse=True)
    for x in sorted_data[:10]:
        print("{}: {}".format(
            x.get('sha'),
            x.get('commit').get('author').get('name')))

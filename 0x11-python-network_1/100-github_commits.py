#!/usr/bin/python3
""" list 10 commits (from the recent to oldest) of the repo 'rails'
by the user 'rails' """
from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2])
    r = get(url)
    data = r.json()[:10]
    for x in data:
        print("{}: {}".format(x['sha'], x['commit']['author']['name']))

#!/usr/bin/python3
""" list 10 commits (from the recent to oldest) of the repo 'rails'
by the user 'rails' """
from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2])
    r = get(url)
    data = r.json()
    sorted_data = sorted(
            data,
            key=lambda d: d.get('commit').get('author').get('date'),
            reverse=True)
    for x in sorted_data[:10]:
        print("{}: {}".format(x['sha'], x['commit']['author']['name']))

#!/usr/bin/python3
""" fetchs https://alx-intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)

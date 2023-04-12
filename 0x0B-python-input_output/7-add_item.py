#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""


import json


if __name__ == "__main__":
    import sys
    import os.path

    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    name = 'add_item.json'
    if os.path.isfile(name):
        arg_list = load_from_json(name)
    else:
        arg_list = []

    for i in range(1, len(sys.argv)):
        arg_list.append(sys.argv[i])

    save_to_json(arg_list, name)

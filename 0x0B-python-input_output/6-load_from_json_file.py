#!/usr/bin/python3
"""Define load_from_json_file function"""


import json


def load_from_json_file(filename):
    """Creates an Object from a \"JSON\"
    Args:
        filename(str): name of the file
    Return:
        the newly created object
    """
    with open(filename, encoding="utf-8") as a_file:
        my_obj = json.loads(a_file.read())
    return my_obj

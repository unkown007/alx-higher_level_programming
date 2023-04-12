#!/usr/bin/python3
"""writes an Object to a text file, using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using JSON representation
    Args:
        my_obj(object): object
        filename(str): name of the file
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write(json.dumps(my_obj))

#!/usr/bin/python3
"""Define read_file funtion"""


def read_file(filename=""):
    """Read a text file(UTF8) and prints it to stdout
    Args:
        filename(str): name of the file
    """
    with open(filename, encoding='utf8') as a_file:
        print(a_file.read(), end="")

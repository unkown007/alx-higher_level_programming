#!/usr/bin/python3
"""Defines append_write funtion"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file(UTF8)
    Args:
        filename(str): name of the file
        text(str): string text
    Returns:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        n = a_file.write(text)
    return n

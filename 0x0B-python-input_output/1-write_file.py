#!/usr/bin/python3
"""Define write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file econding as UTF-8
    Args:
        filename(str): name of the file
        text(str): text to write
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write(text)
        n = a_file.tell()
    return n

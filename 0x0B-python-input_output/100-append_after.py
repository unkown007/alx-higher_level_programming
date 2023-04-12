#!/usr/bin/python3
"""Define append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to file,
    after each line containing a specific string
    Args:
        filename(str): name of the file
        search_string(str): pattern string
        new_string(str): string to insert
    """
    with open(filename, encoding="utf-8") as a_file:
        line = a_file.readline()
        lines = []
        while line != '':
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
            line = a_file.readline()
    with open(filename, "w", encoding="utf-8") as a_file:
        for x in lines:
            a_file.write(x)

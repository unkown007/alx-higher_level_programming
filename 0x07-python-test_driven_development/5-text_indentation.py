#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :
Args:
    text(str): text
"""


def text_indentation(text):
    """Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    symbols = ['.', '?', ':']
    i = 0
    size = len(text)
    while i < size and text[i] == ' ':
        i += 1
    while i < size:
        print("{}".format(text[i]), end="")
        if text[i] == "\n" or text[i] in symbols:
            if text[i] in symbols:
                print("\n")
            i += 1
            while i < size and text[i] == ' ':
                i += 1
            continue
        i += 1

#!/usr/bin/python3
"""Adds two integer numbers
    Args:
        a(int): integer number
        b(int): integer number
"""


def add_integer(a, b=98):
    """  Raises:
            TypeError: if a and is not integer or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

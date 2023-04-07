#!/usr/bin/python3
"""Prints a square with the caracter #

Args:
    size(int): length of the square
"""


def print_square(size):
    """Raises:
        TypeError: if size is not integer
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

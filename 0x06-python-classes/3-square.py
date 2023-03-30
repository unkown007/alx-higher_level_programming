#!/usr/bin/python3
"""This module creates a simple class that defines square
"""


class Square:
    """Defines square
    """
    def __init__(self, size=0):
        """Defines private instance attribute and validate its type

        Args:
            size(int): initialize size value

        Raises:
            TypeError: if size is not int
            ValueError: if size if less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if (size < 0):
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        """Computes area of a square
        """
        return (self.__size ** 2)

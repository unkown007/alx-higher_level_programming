#!/usr/bin/python3
"""Defines sqare class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implements Square class that is derived from rectangle"""

    def __init__(self, size):
        """Initialize object variables
        Args:
            size(int): integer number
        Raises:
            TypeError: if size is not int
            ValueError: if size is less or equal than 0
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a printable string for the object"""
        return f"[Square] {self.__size}/{self.__size}"

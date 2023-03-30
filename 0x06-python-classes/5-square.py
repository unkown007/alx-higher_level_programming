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
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Computes area of a square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Gets the value of the private instance attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set value to the private instance attribute

        Args:
            value(int): integer value to update the private instance attribute

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
        for i in range(0, self.size):
            for j in range(0, self.size):
                print("#", end="")
            print()

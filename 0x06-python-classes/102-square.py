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

    def __eq__(self, other):
        """compares if two objects are equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares if two objects are not equal"""
        return self.area() != other.area()

    def __ge__(self, other):
        """Compares if self object is greater or equal than other object"""
        return self.area() >= other.area()

    def __le__(self, other):
        """Compares if self object is less or equal than other object"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compares if self object is greater than other object"""
        return self.area() > other.area()

    def __lt__(self, other):
        """Compares if self object is less than other object"""
        return self.area() < other.area()

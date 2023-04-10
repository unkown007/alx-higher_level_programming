#!/usr/bin/python3
"""Define a MagicClass that does exactly as the bytecode provided."""


import math


class MagicClass:
    """Represent a circle"""
    def __init__(self, radius=0):
        """Initialize attributes of the object
        Args:
            radius(int or float): a number

        Raises:
            TypeError: if radius is not a number
        """
        self.__radius = 0

        if type(self.radius) is not int and type(self.radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Return the arrea of the cirucumference"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Return the perimeter of the circumference"""
        return 2 * math.pi * self.__radius

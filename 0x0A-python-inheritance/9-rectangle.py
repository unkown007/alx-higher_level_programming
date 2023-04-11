#!/usr/bin/python3
"""Defines a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implements Rectangle"""

    def __init__(self, width, height):
        """Initialize object attributes
        Args:
            width(int): integer number
            height(int): integer number
        Raises:
            TypeError: if width or height is not int
            ValueError: if width or height is less or equal than 0
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Create a object printable string"""
        return f"[Rectangle] {self.__width}/{self.__height}"

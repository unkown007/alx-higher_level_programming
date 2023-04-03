#!/usr/bin/python3
"""Defines a rectangle
"""


class Rectangle:
    """
        This is a Rectangle class

        Attributes:
            number_of_instances(int): integer number of create instances of
            Rectangle class
            print_symbol(any type): represents the output of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize and validades the new object attributes

        Args:
            width(int): integer number
            height(int): integer number

        Raises:
            TypeError: if width or height is not integers
            ValueError: if width or height is less than 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        """width(int): integer object attribute"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        """height(int): integer object attribute"""
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns: the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Returns: the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets object's width with a new value represented by value

        Args:
            value(int): integer number

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets object's height with the new value represented by value

        Args:
            value(int): integer number

        Raises:
            TypeError: if value is not an integer
            ValueError: if valune is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        output = ""
        print(Rectangle.print_symbol)
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                output += str(self.print_symbol)
            if i != (self.__height - 1):
                output += "\n"
        return output

    def __repr__(self):
        """Return string representation to be able to recreate a
        new instance by eval
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Detect instance delection"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

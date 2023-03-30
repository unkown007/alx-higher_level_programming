#!/usr/bin/python3
"""This module creates a simple class that defines square
"""


class Square:
    """Defines square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Defines private instance attribute and validate its type

        Args:
            size(int): initialize size value
            position(tuple): initialize the position(x, y)

        Raises:
            TypeError: if size is not int, or
            if position is not a tuple with 2 positive integers
            ValueError: if size if less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int and type(position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Computes area of a square
        """
        return (self.__size ** 2)

    @property
    def position(self):
        """Gets the position in the square
        """
        return self.__position

    @property
    def size(self):
        """Gets the value of the private instance attribute
        """
        return self.__size

    @position.setter
    def position(self, value):
        """Sets the value to the private instance attribute
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.size):
            for spaces in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.size):
                print("#", end="")
            print("")

#!/usr/bin/python3
"""Defines Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Implements Rectangle class that inherit from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instance attributes
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): x location of the rectangle
            y(int): y location of the rectangle
        Raises:
            TypeError: if width, height, x, y is not integer
            ValueError: if width or height is under or equals to 0,
            or even x or y is  under 0
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """returns the width's value"""
        return self.__width

    @property
    def height(self):
        """returns the height's value"""
        return self.__height

    @property
    def x(self):
        """returns the x's value"""
        return self.__x

    @property
    def y(self):
        """return the x's value"""
        return self.__y

    @width.setter
    def width(self, value):
        """Updates the width's value
        Args:
            value(int): new width's value
        Raises:
            TypeError: if value is not integer
            ValueError: if value is under or equals to 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Updates the height's value
        Args:
            value(int): new height's value
        Raises:
            TypeError: if value is not integer
            ValueError: if value is under or equals to 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Updates the x's value
        Args:
            value(int): new x's value
        Raises:
            TypeError: if value is not integer
            ValueError: if value is  under 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """"Updates the y's value
        Args:
            value(int): new y's value
        Raises:
            TypeError: if value is not integer
            ValueError: if value is  under 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the caracter #
        NB: no need to hangle y and y"""
        [print("") for y in range(self.__y)]
        for y in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            for x in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """assign an argment to each attribute:
            1st - id
            2nd - width
            3rd - height
            4th - x
            5th - y
        Args:
            args(list): list of arguments
        """
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dic = {'x': self.x, 'y': self.y,
                'id': self.id, 'height': self.height, 'width': self.width}
        return dic

    def __str__(self):
        """return a printable string
        \"[Retangle] (<id>) <x>/<y> - <width>/<height>\"
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

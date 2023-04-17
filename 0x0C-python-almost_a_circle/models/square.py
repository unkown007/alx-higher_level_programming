#!/usr/bin/python3
"""Defines Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Implements Square as a subclass of Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize instance attribute
        Args:
            size(int): size of the square
            x(int): x's location of the sqaure
            y(int): y's location of the sqaure
            id(int): instance identifier
        Raises:
            TypeError: if size or x or y is not integer
            ValueError: if size is less or equal than zero,
            or even x or y is less than 0
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size's value"""
        return self.width

    @size.setter
    def size(self, value):
        """Updates the Square instance size attribute
        Args:
            value(int): size of the square
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less or equal than zero
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square instance, assigning attributes:
            1st: id
            2nd: size
            3rd: x
            4th: y
        Args:
            args(list): list of arguments - no-keyworded arguments
            kwargs(dict):  pointer to a dictionary:
            key/value (keyworded arguments)
        Raises:
            TypeError: if size or x or y is not integer
            ValueError: if size is less or equal than zero,
            or even x or y is less than 0
        """
        if args is not None and len(args) > 0:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """return the dictionary representation of a Square"""
        dic = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dic

    def __str__(self):
        """returns a printable Square instance string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

#!/usr/bin/python3
"""Define a Student class"""


class Student:
    """Implements a Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student objects attributes
        Args:
            first_name(str): first name of the student
            last_name(str): last name of the student
            age(int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

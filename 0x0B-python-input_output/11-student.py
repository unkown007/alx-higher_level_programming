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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        Args:
            attrs(list): list of attributes wanted
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for x in attrs:
            if x in self.__dict__:
                new_dict[x] = self.__dict__[x]
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json(dictionary): dictionary object from an instance
        """
        if 'first_name' in json:
            self.first_name = json['first_name']
        if 'last_name' in json:
            self.last_name = json['last_name']
        if 'age' in json:
            self.age = json['age']

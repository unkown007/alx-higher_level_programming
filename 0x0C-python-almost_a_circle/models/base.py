#!/usr/bin/python3
"""Defines Base class"""


import os.path
import json
import models


class Base:
    """Implements the Base class that will serve as the base
    for every other class of this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize object's attributes
        Args:
            id(int): identifier of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionary):
        """returns the JSON string representation of list_dictionaries
        Args:
            list_dictionary(list of dictionary): list of dictionaries
            representing the objects
        Returns: JSON string
        """
        if list_dictionary is None:
            return "[]"
        return json.dumps(list_dictionary)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        Args:
            list_objs(list): list of of objects
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as a_file:
                a_file.write(cls.to_json_string(list_objs))
        else:
            with open(filename, "w", encoding="utf-8") as a_file:
                lis = []
                for obj in list_objs:
                    lis.append(obj.to_dictionary())
                a_file.write(cls.to_json_string(lis))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        Args:
            json_string(str): json string
        Returns:
            list of json string
        """
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            dictionary(dict): double pointer to a dictionary
        Return: new instance
        """
        if cls.__name__ == "Rectangle":
            obj = models.rectangle.Rectangle(1, 1)
            obj.update(**dictionary)
        elif cls.__name__ == "Square":
            obj = models.square.Square(1)
            obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        objs = []
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as a_file:
            string = a_file.read()
        list_dictionary = cls.from_json_string(string)
        for x in list_dictionary:
            objs.append(cls.create(**x))
        return objs

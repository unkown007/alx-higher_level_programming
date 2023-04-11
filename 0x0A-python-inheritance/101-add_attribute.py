#!/usr/bin/python3
"""Defines add_attribute function"""


def add_attribute(obj, name, value):
    """Set new attribute to an object if it's possible
    Args:
        obj(object): Any type of object
        name(string): name of attribute
        value(any): any type of value
    Raises:
        TypeError: if it's not possible to add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

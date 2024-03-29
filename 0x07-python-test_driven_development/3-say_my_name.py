#!/usr/bin/python3
"""prints info

Args:
    first_name(string): first name of the user
    last_name(string): last name of the user
"""


def say_my_name(first_name, last_name=""):
    """Raises:
        TypeError: if first_name or last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
"""Define class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description"""
    return obj.__dict__

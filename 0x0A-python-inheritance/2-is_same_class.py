#!/usr/bin/python3
"""Defines a funtions that checks if an object is a class instance"""


def is_same_class(obj, a_class):
    """Return True if obj is an instance of a_class, False otherwise"""
    return type(obj) is a_class

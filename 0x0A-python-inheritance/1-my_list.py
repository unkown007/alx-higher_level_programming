#!/usr/bin/python3
"""Defines a MyList class that inherits from list"""


class MyList(list):
    """Implements a MyList class that inherits from list"""

    def print_sorted(self):
        """Prints a sorted list in asceding order"""
        li = super().copy()
        li.sort()
        print(li)

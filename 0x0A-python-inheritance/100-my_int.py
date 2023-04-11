#!/usr/bin/python3
"""Define Myint class"""


class MyInt(int):
    """Implements Myint"""

    def __eq__(self, other):
        """compares two objects if are equals"""
        return (not super().__eq__(other))

    def __ne__(self, other):
        """compares two objects if are different"""
        return (not super().__ne__(other))

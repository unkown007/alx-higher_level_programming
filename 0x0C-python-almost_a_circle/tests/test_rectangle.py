#!/usr/bin/python3
"""Unit test class Rectangle"""
import unittest
import json
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Class of functions to run tests
    """

    def setUp(self):
        """
        function to redirect stdout
        """
        sys.stdout = StringIO()

    def tearDown(self):
        """
        cleans everything
        """
        sys.stdout = sys.__stdout__

    def test_object(self):
        self.assertIs(type(Rectangle(1, 2)), Rectangle)

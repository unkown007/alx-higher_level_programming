#!/usr/bin/python3
"""Module to test the function rectangle"""
import unittest
import rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_output(self):
        """Function to test the output the function rectangle"""

        self.assertAlmostEqual(rectangle(,))

    def test_rectangle_input(self):
        """Function to test the input the function rectangle"""

        self.assertRaises(TypeError, rectangle, )

    def test_rectangle_object(self):
        """Fucntion to test the rectangle object creation"""
        self.assertIs(type(rectangle(1, 2)), rectangle)

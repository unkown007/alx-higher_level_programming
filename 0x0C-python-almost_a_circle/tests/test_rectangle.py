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
        #sys.stdout = StringIO()

    def tearDown(self):
        """
        cleans everything
        """
        #sys.stdout = sys.__stdout__

    def test_object_1(self):
        self.assertIs(type(Rectangle(1, 2)), Rectangle)

    def test_object_2(self):
        self.assertIs(type(Rectangle(1, 2, 3)), Rectangle)

    def test_object_3(self):
        self.assertIs(type(Rectangle(1, 2, 3, 4)), Rectangle)

    def test_object_4(self):
        self.assertRaises(TypeError, Rectangle, "1", 2)

    def test_object_5(self):
        self.assertRaises(TypeError, Rectangle, 1, "2")

    def test_object_6(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")

    def test_object_7(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    def test_object_8(self):
        self.assertRaises(ValueError, Rectangle, -1, 2)

    def test_object_9(self):
        self.assertRaises(ValueError, Rectangle, 1, -2)

    def test_object_10(self):
        self.assertRaises(ValueError, Rectangle, 0, 2)

    def test_object_11(self):
        self.assertRaises(ValueError, Rectangle, 1, 0)

    def test_object_12(self):
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)

    def test_object_13(self):
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_area(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.area(), 2)

    def test_str(self):
        obj = Rectangle(1, 2, id=1)
        string = obj.__str__()
        self.assertEqual(string, "[Rectangle] (1) 0/0 - 1/2")

    def test_display_1(self):
        tmp = sys.stdout
        result = StringIO()
        sys.stdout = result
        obj = Rectangle(2, 2)
        obj.display()
        sys.stdout = tmp
        output = "##\n##\n"
        self.assertEqual(result.getvalue(), output)

    def test_display_2(self):
        tmp = sys.stdout
        result = StringIO()
        sys.stdout = result
        obj = Rectangle(2, 2, 1)
        obj.display()
        sys.stdout = tmp
        output = " ##\n ##\n"
        self.assertEqual(result.getvalue(), output)

    def test_display_3(self):
        tmp = sys.stdout
        result = StringIO()
        sys.stdout = result
        obj = Rectangle(2, 2, 1, 1)
        obj.display()
        sys.stdout = tmp
        output = "\n ##\n ##\n"
        self.assertEqual(result.getvalue(), output)

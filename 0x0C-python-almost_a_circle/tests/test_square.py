#!/usr/bin/python3
"""Unit test class Square"""
import unittest
from models.square import Square
import sys
from io import StringIO


class TestSquare(unittest.TestCase):
    """
    class of functions to run tests
    """

    def setUp(self):
        """
        function to redirect stdout
        """
        #sys.stdout = StringIO()

    def tearDown(self):
        """
        Cleans everything
        """
        #sys.stdout = sys.__stdout__

    def test_object_1(self):
        self.assertIs(type(Square(1)), Square)

    def test_object_2(self):
        self.assertIs(type(Square(1, 2)), Square)

    def test_object_3(self):
        self.assertIs(type(Square(1, 2, 3)), Square)

    def test_object_4(self):
        self.assertRaises(TypeError, Square, "1")

    def test_object_5(self):
        self.assertRaises(TypeError, Square, 1, "2")

    def test_object_6(self):
        self.assertRaises(TypeError, Square, 1, 2, "3")

    def test_object_7(self):
        self.assertIs(type(Square(1, 2, 3, 4)), Square)

    def test_object_8(self):
        self.assertRaises(ValueError, Square, -1)

    def test_object_9(self):
        self.assertRaises(ValueError, Square, 1, -2)

    def test_object_10(self):
        self.assertRaises(ValueError, Square, 1, 2, -3)

    def test_object_11(self):
        self.assertRaises(ValueError, Square, 0)

    def test_str(self):
        obj = Square(1, id=1)
        string = obj.__str__()
        self.assertEqual(string, "[Square] (1) 0/0 - 1")

    def test_dictionary(self):
        obj = Square(1, id=1)
        dic = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        self.assertEqual(obj.to_dictionary(), dic)


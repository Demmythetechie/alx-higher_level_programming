#!/usr/bin/python3
""" This module contains the unitest of square """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class SquareTest10(unittest.TestCase):
    """
    This test if the inheritance of Rectangle class into
    the Square Class and the modification of the __str__
    method is succesful

    """

    def test_correct(self):
        sq1 = "#####\n"\
                "#####\n"\
                "#####\n"\
                "#####\n"\
                "#####\n"

        sq2 = "\n"\
              "    ######\n"\
              "    ######\n"\
              "    ######\n"\
              "    ######\n"\
              "    ######\n"\
              "    ######\n"

        s1 = Square(5)
        self.assertEqual(s1.id, 23)
        self.assertEqual(s1.display(), sq1)
        self.assertEqual(str(s1), "[Square] (23) 0/0 - 5")
        self.assertEqual(s1.area(), 25)

        s2 = Square(6, 4, 1)
        self.assertEqual(str(s2), "[Square] (24) 4/1 - 6")
        self.assertEqual(s2.display(), sq2)
        self.assertEqual(s2.id, 24)
        self.assertEqual(s2.area(), 36)

    def test_error_bound(self):
        """
        This shows error bound operations of class square
        """

        with self.assertRaises(TypeError):
            s3 = Square()


class SquareTest11(unittest.TestCase):
    """
    This test the implementation of size getter and setter
    for width and height
    """

    def test_correct_output(self):
        """
        This test expected output of the implementation
        """

        s3 = Square(5)
        self.assertEqual(str(s3), "[Square] (25) 0/0 - 5")
        self.assertEqual(s3.size, 5)
        self.assertEqual(s3.height, 5)
        s3.size = 20
        self.assertEqual(s3.size, 20)
        self.assertEqual(str(s3), "[Square] (25) 0/0 - 20")
        self.assertEqual(s3.width, 20)

    def test_error_bound(self):
        """
        Testing for error bound output
        """

        with self.assertRaises(TypeError):
            s4 = Square('3')

        with self.assertRaises(ValueError):
            s4 = Square(0)

        s4 = Square(3)
        self.assertEqual(s4.id, 26)

        with self.assertRaises(TypeError):
            s4.size = '9'

        with self.assertRaises(ValueError):
            s4.size = -9

        with self.assertRaises(ValueError):
            s4.size = 0


class SquareTest12(unittest.TestCase):
    """
    This class tests the implementation of update
    which overrides the update method of class Rectangle
    """

    def test_correct(self):
        """
        This test expected output of the implementation
        """

        s5 = Square(5)
        self.assertEqual(s5.id, 27)
        self.assertEqual(str(s5), "[Square] (27) 0/0 - 5")

        s5.update(10)
        self.assertEqual(str(s5), "[Square] (10) 0/0 - 5")
        self.assertEqual(s5.id, 10)

        s5.update(1, 2, 3, 4)
        self.assertEqual(str(s5), "[Square] (1) 3/4 - 2")
        self.assertEqual(s5.id, 1)

        s5.update(size=5, id=90)
        self.assertEqual(str(s5), "[Square] (90) 3/4 - 5")

        s5.update(10, 7, 2, 9, 2, 0)
        self.assertEqual(str(s5), "[Square] (10) 2/9 - 7")

        s5.update(size=5, x=10, width=2)
        self.assertEqual(str(s5), "[Square] (10) 10/9 - 5")

    def test_error_bound(self):
        """
        Testing for error bound output
        """

        with self.assertRaises(TypeError):
            s6 = Square(2, 3, 4, 45, 98)


class SquareTest13(unittest.TestCase):
    """
    This class test the implementation of
    to_dictuionary which overrided that of Rectangle
    class
    """

    def test_correct(self):
        """
        This tests expected output of the implementation
        """

        s6 = Square(5, 2, 1)
        self.assertEqual(s6.id, 28)
        self.assertEqual(str(s6), "[Square] (28) 2/1 - 5")
        s1_dict = s6.to_dictionary()
        self.assertEqual(s1_dict, {'id': 28, 'x': 2, 'size': 5, 'y': 1})
        self.assertIsInstance(s1_dict, dict)

        s6.update(90, 5, 20, 2)
        self.assertEqual(s6.id, 90)
        self.assertEqual(str(s6), "[Square] (90) 20/2 - 5")
        s2_dict = s6.to_dictionary()
        self.assertEqual(s2_dict, {'id': 90, 'x': 20, 'size': 5, 'y': 2})

        s7 = Square(2, 5, 2, 3)
        self.assertEqual(s7.id, 3)
        self.assertEqual(str(s7), "[Square] (3) 5/2 - 2")
        s7.update(**s1_dict)
        self.assertEqual(str(s7), "[Square] (28) 2/1 - 5")
        s3_dict = s7.to_dictionary()
        self.assertTrue(s1_dict == s3_dict)
        self.assertFalse(s2_dict == s1_dict)

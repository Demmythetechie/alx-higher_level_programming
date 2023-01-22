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

        sq3 = "\n"\
                "  #####\n"\
                "  #####\n"\
                "  #####\n"\
                "  #####\n"\
                "  #####\n"

        sq4 = "\n"\
                "\n"\
                "  ######\n"\
                "  ######\n"\
                "  ######\n"\
                "  ######\n"\
                "  ######\n"\
                "  ######\n"

        s1 = Square(5)
        self.assertEqual(s1.id, 23)
        self.assertEqual(s1.display(), sq1)
        s1.update(23, 8, 8, 2)
        self.assertEqual(str(s1), "[Square] (23) 2/0 - 8")
        s1.update(90, 6, 6, 4, 1)
        self.assertEqual(str(s1), "[Square] (90) 4/1 - 6")
        self.assertEqual(s1.id, 90)
        self.assertEqual(s1.display(), sq2)
        s1.update(90, 5, 5, 2)
        self.assertEqual(s1.id, 90)
        self.assertEqual(s1.display(), sq3)
        self.assertEqual(s1.area(), 25)

        s2 = Square(6, 4, 1)
        self.assertEqual(str(s2), "[Square] (24) 4/1 - 6")
        self.assertEqual(s2.display(), sq2)
        self.assertEqual(s2.id, 24)
        s2.update(x=2, y=2, id=50)
        self.assertEqual(s2.id, 50)
        self.assertEqual(s2.display(), sq4)
        self.assertEqual(s2.area(), 36)

    def test_error_bound(self):
        """
        This shows error bound operations of class square
        """

        with self.assertRaises(TypeError):
            s3 = Square()

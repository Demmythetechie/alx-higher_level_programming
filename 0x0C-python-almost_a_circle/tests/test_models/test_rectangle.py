#!/usr/bin/python3
"""This is the unitest for class rectangle"""


import unittest
from models.base import Base
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):
    """
        pos means positive
        neg mean negative
    """

    def test_base_inherit_pos(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
        r2 = Rectangle(14, 2)
        self.assertEqual(r2.id, 1)

    def test_base_neg_inherit(self):
        with self.assertRaises(ValueError):
            r3 = Rectangle(24, 4, 0, 0, -12)
        r4 = Rectangle(24, 4)
        self.assertEqual(r4.id, 2)

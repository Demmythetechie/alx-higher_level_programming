#!/usr/bin/python3
"""Unit test for Base class"""
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """This class contains various test cases on class Base"""

    def test_no_integer(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_positive_int(self):
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b5 = Base(12)
        self.assertEqual(b5.id, 12)
        b6 = Base()
        self.assertEqual(b6.id, 5)

    def test_negative_int(self):
        with self.assertRaises(ValueError):
            b1 = Base(-12)

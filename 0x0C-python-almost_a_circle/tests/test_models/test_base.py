#!/usr/bin/python3
"""Unit test for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This class contains various test cases on class Base"""

    def test_of_base(self):
        """
        Test of Base() for assigning
        automatically an ID exists
        """

        b1 = Base()
        self.assertEqual(b1.id, 1)


if __name__ == "__main__":
    unittest.main()

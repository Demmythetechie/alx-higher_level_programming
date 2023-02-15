#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer(list=[]))

    def test_corect_output(self):
        self.assertEqual(max_integer(list=[1, 2, 3, 4]), 4)
        self.assertEqual(max_integer(list=[1, 2, 3.7, 10.2, 4]), 10.2)
        self.assertEqual(max_integer(list=['str', 'jsn']), 'str')

#!/usr/bin/python3
"""This is the unitest for class rectangle"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleAttrIdTest(unittest.TestCase):
    """
        pos means positive
        neg mean negative

        Test:
            test_base_inherit_pos
            test_base_neg_inherit
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


class RectangleMainAttrTest(unittest.TestCase):
    """
    This class test the attribute of class Rectangle
    if it works as planned

    TestCases:
        test_for_attr_width
        test_for_height_attr
        test_for_x_attr
        test_for_y_attr
    """

    def test_for_attr_width(self):
        """
        Testing required function expected from attribute width
        including:
            input through instantiation
            input from setter
            manipulation of setter

        """

        w1 = Rectangle(21, 9)
        self.assertEqual(w1.width, 21)
        w1.width = 3
        self.assertEqual(w1.width, 3)
        w1.width = w1.width - 2
        self.assertEqual(w1.width, 1)

        """
        Testing for input faluire:
            TypeError: list, str, tuple, dic, double
            valueError: negative values and zero

        """

        with self.assertRaises(ValueError):
            w2 = Rectangle(-34, 3)
        with self.assertRaises(ValueError):
            w2 = Rectangle(0, 34)
        with self.assertRaises(TypeError):
            w2 = Rectangle(72.3, 3)
        with self.assertRaises(TypeError):
            w2 = Rectangle('ekme', 3)
        with self.assertRaises(TypeError):
            w2 = Rectangle([2], 3)
        with self.assertRaises(TypeError):
            w2 = Rectangle((2, 3, 5), 3)
        with self.assertRaises(TypeError):
            w2 = Rectangle({'width': 4}, 3)

        """Testing for id:"""

        w2 = Rectangle(34, 3)
        w1.width = w2.width + w1.width
        self.assertEqual(w1.width, 35)
        self.assertEqual(w2.id, 4)

    def test_for_height_attr(self):
        """
        Testing required function expected from attribute height
        including:
            input through instantiation
            input from setter
            manipulation of setter

        """
        h1 = Rectangle(21, 9)
        self.assertEqual(h1.height, 9)
        h1.height = 3
        self.assertEqual(h1.height, 3)
        h1.height = h1.height - 2
        self.assertEqual(h1.height, 1)

        """
        Testing for input faluire:
            TypeError: list, str, tuple, dic, double
            valueError: negative values and zero

        """

        with self.assertRaises(ValueError):
            h2 = Rectangle(3, -34)
        with self.assertRaises(ValueError):
            h2 = Rectangle(3, 0)
        with self.assertRaises(TypeError):
            h2 = Rectangle(3, 72.3)
        with self.assertRaises(TypeError):
            h2 = Rectangle(3, 'ekme')
        with self.assertRaises(TypeError):
            h2 = Rectangle(3, [2])
        with self.assertRaises(TypeError):
            h2 = Rectangle(3, (2, 3, 5))
        with self.assertRaises(TypeError):
            h2 = Rectangle(3, {'height': 4})

        """Testing for id:"""

        h2 = Rectangle(34, 3)
        h1.height = h2.height + h1.height
        self.assertEqual(h1.height, 4)
        self.assertEqual(h2.id, 6)

    def test_for_x_attr(self):
        """
        Testing required function expected from attribute x
        including:
            input through instantiation
            input from setter
            manipulation of setter

        """
        x1 = Rectangle(21, 9)
        self.assertEqual(x1.x, 0)
        x1.x = 3
        self.assertEqual(x1.x, 3)
        x1.x = x1.x - 2
        self.assertEqual(x1.x, 1)

        """
        Testing for input faluire:
            TypeError: list, str, tuple, dic, double
            valueError: negative values

        """

        with self.assertRaises(ValueError):
            x2 = Rectangle(3, 34, -34)
        with self.assertRaises(TypeError):
            x2 = Rectangle(3, 45, 72.3)
        with self.assertRaises(TypeError):
            x2 = Rectangle(3, 56, 'ekme')
        with self.assertRaises(TypeError):
            x2 = Rectangle(3, 66, [2])
        with self.assertRaises(TypeError):
            x2 = Rectangle(3, 65, (2, 3, 5))
        with self.assertRaises(TypeError):
            x2 = Rectangle(3, 44, {'x': 4})

        """Testing for id:"""

        x2 = Rectangle(34, 3, 8)
        x1.x = x2.x + x1.x
        self.assertEqual(x1.x, 9)
        self.assertEqual(x2.id, 8)

    def test_for_y_attr(self):
        """
        Testing required function expected from attribute y
        including:
            input through instantiation
            input from setter
            manipulation of setter

        """

        y1 = Rectangle(21, 9)
        self.assertEqual(y1.y, 0)
        y1.y = 3
        self.assertEqual(y1.y, 3)
        y1.y = y1.y - 2
        self.assertEqual(y1.y, 1)

        """
        Testing for input faluire:
            TypeError: list, str, tuple, dic, double
            valueError: negative values

        """

        with self.assertRaises(ValueError):
            y2 = Rectangle(3, 34, 83, -34)
        with self.assertRaises(TypeError):
            y2 = Rectangle(3, 45, 83, 72.3)
        with self.assertRaises(TypeError):
            y2 = Rectangle(3, 56, 89, 'ekme')
        with self.assertRaises(TypeError):
            y2 = Rectangle(3, 66, 84, [2])
        with self.assertRaises(TypeError):
            y2 = Rectangle(3, 65, 63, (2, 3, 5))
        with self.assertRaises(TypeError):
            y2 = Rectangle(3, 44, 84, {'y': 4})

        """Testing for id:"""

        y2 = Rectangle(34, 3, 8, 4)
        y1.y = y2.y + y1.y
        self.assertEqual(y1.y, 5)
        self.assertEqual(y2.id, 10)


class RectangleTaskThree(unittest.TestCase):

    def test_for_3_task_area(self):
        """
        Testing for area of a rectangle
        using attribute width and height
        """

        area1 = Rectangle(30, 2)
        self.assertEqual(area1.area(), 60)

        with self.assertRaises(ValueError):
            area2 = Rectangle(-5, 2)
            self.assertEqual(area2.area(), -10)

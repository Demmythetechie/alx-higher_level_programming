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
        self.assertEqual(r2.id, 6)

    def test_base_neg_inherit(self):
        with self.assertRaises(ValueError):
            r3 = Rectangle(24, 4, 0, 0, -12)
        r4 = Rectangle(24, 4)
        self.assertEqual(r4.id, 7)


class RectangleTask3(unittest.TestCase):
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
        self.assertEqual(w2.id, 9)

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
        self.assertEqual(h2.id, 11)

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
        self.assertEqual(x2.id, 13)

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
        self.assertEqual(y2.id, 15)


class RectangleTask4(unittest.TestCase):

    def test_for_area(self):
        """
        Testing for area of a rectangle
        using attribute width and height
        """

        area1 = Rectangle(30, 2)
        self.assertEqual(area1.area(), 60)

        with self.assertRaises(ValueError):
            area2 = Rectangle(-5, 2)
            self.assertEqual(area2.area(), -10)

        with self.assertRaises(TypeError):
            area2 = Rectangle(5, 2)
            self.assertEqual(area2.area(5), 10)

        with self.assertRaises(TypeError):
            area2 = Rectangle(3)


class RectangleTask5(unittest.TestCase):
    """
        This test the display method
    """

    def test_for_display(self):
        """
        Testing for display of a rectangle
        using attribute width and height
        """
        st_d1 = "####\n"\
                "####\n"\
                "####\n"\
                "####\n"

        d1 = Rectangle(4, 4)
        self.assertEqual(d1.display(), st_d1)

    def test_for_incorect_display(self):
        """
        This test incorrect cases for display method
        including:
            Missing height argument
            argument in display method
        """
        st_d2 = "####\n"\
                "####\n"\
                "####\n"\
                "####\n"

        with self.assertRaises(TypeError):
            d2 = Rectangle(4, 4)
            self.assertEqual(d2.display(5), st_d2)

        with self.assertRaises(TypeError):
            d2 = Rectangle(4)


class RectangleTask6(unittest.TestCase):
    """
    This class tests correct and error bound cases
    for __str__ method in Rectangle class
    """

    def test_correct_output(self):

        """
        This method tests expected function
        for __str__ method in Rectangle class
        """

        st = Rectangle(10, 5, 0, 1, 19)
        self.assertEqual(st.__str__(), "[Rectangle] (19) 0/1 - 10/5")

    def test_error_output(self):
        """
        This method tests error bound cases
        for __str__ method in Rectangle class
        """

        st_1 = Rectangle(10, 5, 0, 1, 19)
        with self.assertRaises(TypeError):
            self.assertEqual(st_1.__str__(3), "[Rectangle] (19) 0/1 - 10/5")


class RectangleTest7(unittest.TestCase):
    """
    This class test the implemention of display
    """

    def test_new_display(self):
        st1 = "\n"\
                "\n"\
                "\n"\
                "\n"\
                "     ####\n"\
                "     ####\n"\
                "     ####\n"

        d3 = Rectangle(4, 3, 5, 4)
        self.assertEqual(d3.display(), st1)


class RectangleTest8(unittest.TestCase):
    """
    This class test the implementation of update
    """

    def test_correct_out(self):
        u1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(u1), "[Rectangle] (21) 10/10 - 10/10")

        u1.update(89)
        self.assertEqual(str(u1), "[Rectangle] (89) 10/10 - 10/10")

        u1.update(89, 2)
        self.assertEqual(str(u1), "[Rectangle] (89) 10/10 - 2/10")

        u1.update()
        self.assertEqual(str(u1), "[Rectangle] (89) 10/10 - 2/10")

        u1.update(89, 2, 3)
        self.assertEqual(str(u1), "[Rectangle] (89) 10/10 - 2/3")

        u1.update(89, 2, 3, 4)
        self.assertEqual(str(u1), "[Rectangle] (89) 4/10 - 2/3")

        u1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(u1), "[Rectangle] (89) 4/5 - 2/3")


class RectangleTest9(unittest.TestCase):
    """
    This class tests the implementation of update method
    with new implementation of **kwargs argument.
    if *args does not contain any element
    it will use the elements in kwargs else
    uses the default value passed to the init method
    """

    def test_correct(self):
        """
        This test for expected output
        """

        u2 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(u2), "[Rectangle] (22) 10/10 - 10/10")

        u2.update(height=1)
        self.assertEqual(str(u2), "[Rectangle] (22) 10/10 - 10/1")

        u2.update(width=1, x=2)
        self.assertEqual(str(u2), "[Rectangle] (22) 2/10 - 1/1")

        u2.update()
        self.assertEqual(str(u2), "[Rectangle] (22) 2/10 - 1/1")

        u2.update(89, 2, 3, 4, 5)
        self.assertEqual(str(u2), "[Rectangle] (89) 4/5 - 2/3")

        u2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(u2), "[Rectangle] (89) 3/1 - 2/3")

        u2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(u2), "[Rectangle] (89) 1/3 - 4/2")


class RectangleTest13(unittest.TestCase):
    """
    This class tests the implementation of to_dictionary
    method. which prints the attribute of class Rectangle
    """

    def test_correct(self):
        """
        This test for expected output
        """

        r1 = Rectangle(10, 5, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (9) 2/1 - 10/5")
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, {'x': 2,
                                   'y': 1,
                                   'id': 9,
                                   'height': 5,
                                   'width': 10
                                   })
        self.assertIsInstance(r1_dict, dict)

        r1.update(90, 10, 5, 4, 2)
        self.assertEqual(str(r1), "[Rectangle] (90) 4/2 - 10/5")
        r2_dict = r1.to_dictionary()
        self.assertEqual(r2_dict, {'x': 4,
                                   'y': 2,
                                   'id': 90,
                                   'height': 5,
                                   'width': 10
                                   })

        r2 = Rectangle(20, 10, 10, 5, 89)
        self.assertEqual(str(r2), "[Rectangle] (89) 10/5 - 20/10")
        r2.update(**r1_dict)
        self.assertEqual(str(r2), "[Rectangle] (9) 2/1 - 10/5")
        r3_dict = r2.to_dictionary()
        self.assertTrue(r1_dict == r3_dict)
        self.assertFalse(r2_dict == r1_dict)


if __name__ == "__main__":
    unittest.main()

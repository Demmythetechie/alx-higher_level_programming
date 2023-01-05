#!/usr/bin/python3
"""
    Created a class 'Rectangle' with two private attribute
    'width and height' to build a rectangle.

    Then created two public method 'area and perimeter' that
    returns the area and perimeter of a rectangle using width
    and height respectively.

    Created a str method that return a rectangle constructed
    with #

    Created a repr method which returns the instance
    representation of a class

    Created a public class attribute which is being updated when
    an instance is created or deleted
"""


class Rectangle:
    """
        The rectangle class creates two private attribute
        along with a getter and setter for them both

        Args:
            number_of_instances (int): class attribute for
            numbers of instances created from this class

            print_symbol (None): class attrbutes for string
            reprsentation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Two private attributes are being intialised

            Args:
                Width (int): width of a rectangle
                Height (int): height of a rectangle

        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ This is the getter for width """

        return self.__width

    @width.setter
    def width(self, value):
        """
            This is the setter for width

            Args:
                value (int): width will contain value

        """

        try:
            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        except (TypeError, ValueError):
            raise

    @property
    def height(self):
        """ This is the getter for height attribute """

        return self.__height

    @height.setter
    def height(self, value):
        """
            This is the setter for height

            Args:
                value (int): height will contain value

        """

        try:
            if type(value) != int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        except (TypeError, ValueError):
            raise

    def area(self):
        """ This method calculates the area of a rectangle """

        ar = self.__width * self.__height
        return ar

    def perimeter(self):
        """This methood calculates the perimeter of a rectangle"""

        if self.__height != 0 or self.__width != 0:
            prm = self.__width * 2 + self.__height * 2
        else:
            prm = 0
        return prm

    def __str__(self):
        """ This method return a rectangle constructed with # """

        s = ''
        if self.__height != 0 or self.__width != 0:
            for i in range(self.__height):
                for x in range(self.__width):
                    s += "{}".format(self.print_symbol)
                if i != self.__height - 1:
                    s += '\n'
        else:
            s = ''
        return s

    def __repr__(self):
        """ This method returns a string representation of the class """

        st = "Rectangle({}, {})".format(self.__width, self.__height)
        return st

    def __del__(self):
        """This method returns a message after an instance as been deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This is a static method returns the biggest rectangle"""

        try:
            if type(rect_1) != Rectangle:
                raise TypeError("rect_1 must be an instance of Rectangle")
            elif type(rect_2) != Rectangle:
                raise TypeError("rect_2 must be an instance of Rectangle")
            elif rect_1.area() > rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            else:
                return rect_1
        except TypeError:
            raise

    @classmethod
    def square(cls, size=0):
        """Returns a rectangle instance with width==height==size"""
        
        return cls(size, size)

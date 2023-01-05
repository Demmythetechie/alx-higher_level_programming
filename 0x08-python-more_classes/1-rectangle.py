#!/usr/bin/python3
"""
    Create a class 'Rectangle' with two private attribute
    'width and height' to build a rectangle
"""


class Rectangle:
    """
        The rectangle class creates two private attribute
        along with a getter and setter for them both
    """

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
        except(TypeError, ValueError):
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
        except(TypeError, ValueError):
            raise

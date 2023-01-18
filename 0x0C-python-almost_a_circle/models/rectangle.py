#!/usr/bin/python3
"""This module contains a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Yet to know the function of this class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Five attribute have been instantiated including id
            for Base class

            Args:
                width (int) : width is assigned to self.__width
                height (int) : height is assigned to self.__height
                x (int) : x is assigned to self.__x
                y (int) : y is assigned to self.__y
                id (int) : id is assigned to init for base

        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """This is the getter for width"""

        return self.__width

    @width.setter
    def width(self, width):
        """
            This is the setter for attribute width.

            Args:
                width (int) : width is assigned self.__width

        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """This is the getter for height"""

        return self.__height

    @height.setter
    def height(self, height):
        """
            This is the setter for attribute height.

            Args:
                height (int) : height is assigned self.__height

        """

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """This is the getter for x"""

        return self.__x

    @x.setter
    def x(self, x):
        """
            This is the setter for attribute x.

            Args:
                x (int) : x is assigned self.__x

        """

        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """This is the getter for y"""

        return self.__y

    @y.setter
    def y(self, y):
        """
            This is the setter for attribute y.

            Args:
                y (int) : y is assigned self.__y

        """

        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
            This method caculates the area of a rectangle
            using the following attribute:
            width and height
        """

        return self.__width * self.__height

    def display(self):
        """
            Use Width and Height to construct a rectangle shape
        """

        st = ''
        for x in range(self.__height):
            for i in range(self.__width):
                st += '#'
            if x != self.__height:
                st += '\n'
        print(st, end='')
        return st

    def __str__(self):
        """
        This method changes the output of an object from
        the location of the object format to format
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """

        return ("[Rectangle] ({}) {}/{} - {}/{}"
              .format(self.id, self.__x,
                      self.__y, self.__width, self.__height))

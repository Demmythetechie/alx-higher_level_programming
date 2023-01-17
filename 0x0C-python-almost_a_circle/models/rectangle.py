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

        self.__width = width
        self.__height = height
        self.__x = x 
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

        self.__y = y

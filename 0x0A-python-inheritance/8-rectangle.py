#!/usr/bin/python3
"""This module contains a sub class that inherits BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This intializes private atrribute width and height"""

    def __init__(self, width, height):
        """ This intializes private atrribute width and height """

        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

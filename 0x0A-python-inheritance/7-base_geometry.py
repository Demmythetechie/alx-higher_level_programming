#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


class BaseGeometry:
    """ Created an empty class BaseGeometry """

    def area(self):
        """ raise an exception upon creation of method area()"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates whether value is type int and >= 0"""

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return True

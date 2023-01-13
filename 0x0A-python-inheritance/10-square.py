#!/usr/bin/python3
""" This module bears a square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class caculates somes square properties"""

    def __init__(self, size):
        """
            This method instantiate argument 'size'
            which is to be used for width and height
            of the rectangle class 'area method'
            to caculate the area of a square
        """

        if self.integer_validator("size", size):
            super().__init__(size, size)

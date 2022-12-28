#!/usr/bin/python3
"""The class square is imported"""


class Square:
    """This class after creating an attribute"""

    def __init__(self, size=0):
        """ this intializes size

        Args:
            size (int): a private instance attribute

        """

        try:
            if size != int(size):
                raise TypeError("size not integer")
            elif size < 0:
                raise ValueError("size < 0")
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

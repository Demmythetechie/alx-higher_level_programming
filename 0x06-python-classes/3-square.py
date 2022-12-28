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
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            raise
        except ValueError:
            raise

    def area(self):
        """This squares the integer passed to size"""

        self.__size = self.__size ** 2
        return self.__size

#!/usr/bin/python3
""" This imports Square class """


class Square:
    """ This class caculate the square """

    def __init__(self, size=0):
        """ size variable was intialized

        Args:
            size (int): This carry out operation of a square

        """
        try:
            if type(size) != int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            raise
        except ValueError:
            raise

    @property
    def size(self):
        """ This is a getter for size attribute """

        return self.__size

    @size.setter
    def size(self, value):
        """ This is the setter for size attribute

        Args:
            value (int): This helps with the modificationin setter

        """

        try:
            if type(value) != int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        except TypeError:
            raise
        except ValueError:
            raise

    def area(self):
        """This method returns the square of size"""

        s = self.__size ** 2
        return s

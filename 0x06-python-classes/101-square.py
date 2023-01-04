#!/usr/bin/python3
""" This imports Square class """


class Square:
    """ This class caculate the square """

    def __init__(self, size=0, position=(0, 0)):
        """ size variable was intialized
        Args:
            size (int): This carry out operation of a square
            position (tuple): second
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

        try:
            if len(position) != 2:
                raise TypeError('position must be a tuple '
                                'of 2 positive integers')
            elif type(position[0]) != int or type(position[1]) != int:
                raise TypeError('position must be a tuple '
                                'of 2 positive integers')
            elif position[0] < 0 or position[1] < 0:
                raise TypeError('position must be a tuple '
                                'of 2 positive integers')
            else:
                self.__position = position
        except TypeError:
            raise

    @property
    def size(self):
        """ This is a getter for size attribute """

        return self.__size

    @size.setter
    def size(self, value):
        """ This is the setter for size attribute
        Args:
            value (int): This helps with the modification in setter
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

    @property
    def position(self):
        """ Getter for attribute position """

        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for attribute position
        Args:
            value (tuple): This helps with the modificationin setter
        """

        try:
            if len(value) != 2:
                raise TypeError('position must be a tuple '
                                'of 2 positive integers')
            elif type(value) != int or type(value) != int:
                raise TypeError('position must be a tuple '
                                'of 2 positive integers')
            elif value[0] < 0 or value[1] < 0:
                raise TypeError('position must be a tuple '
                                'of 2 positive integers')
            else:
                self.__position = value
        except TypeError:
            raise

    def area(self):
        """This method returns the square of size"""

        s = self.__size ** 2
        return s


    if __name__ == '__main__':
        def my_print(self):
            """ This method prints the square of size using # """

            if self.__size != 0:
                for i in range(self.__position[1]):
                    print()
                for i in range(self.__size):
                    for y in range(self.__position[0]):
                        print(" ", end='')
                    for i in range(self.__size):
                        print("#", end='')
                    print()
            else:
                print()

#!/usr/bin/python3
""" This modules contain Square class """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the constructor for class square
        for attribute being inherited from Rectangle

        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This method changes the output of an object from
        the location of the object format to format
        [Square] (<id>) <x>/<y> - <width>/<height>
        """

        self.update()
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

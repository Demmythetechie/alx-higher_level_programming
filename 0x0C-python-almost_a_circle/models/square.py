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

    @property
    def size(self):
        """
        This is the getter for size attribute
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        This is the setter for size to width and height
        """

        if type(size) != int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
            self.height = size

    def __str__(self):
        """
        This method changes the output of an object from
        the location of the object format to format
        [Square] (<id>) <x>/<y> - <width>/<height>
        """

        self.update()
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """
        This update method overrides update method
        from the class Rectangle
        """

        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'size' in kwargs:
                self.size = kwargs.get('size')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """
        This method returns a dictionary of all the attribute
        including the inherited ones of class Square
        """

        dic = {
            'id': getattr(self, 'id'),
            'x': getattr(self, 'x'),
            'size': getattr(self, 'size'),
            'y': getattr(self, 'y'),
        }

        return dic

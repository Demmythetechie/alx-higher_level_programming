#!/usr/bin/python3
""" This module contains a class for now"""


class Base:
    """
        This class will be the “base” of all other classes in this project.
        The goal of it is to manage id attribute in all your future classes
        and to avoid duplicating the same code (by extension, same bugs)

        Args:
            __nb_object (int):
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            if id < -1:
                raise ValueError("id cannot be negative")
            else:
                self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

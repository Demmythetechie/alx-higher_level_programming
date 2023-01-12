#!/usr/bin/python3
""" This module checks is an object is of a class"""


def is_kind_of_class(obj, a_class):
    """
        This function return true if obj is of a_class
        otherwise false
    """

    return isinstance(obj, a_class)

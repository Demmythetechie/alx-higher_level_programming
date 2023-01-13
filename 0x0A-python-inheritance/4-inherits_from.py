#!/usr/bin/python3
"""This module tell is instance or not"""


def inherits_from(obj, a_class):
    """
        This function return true if obj is instance of
        a_class . otherwise False
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False

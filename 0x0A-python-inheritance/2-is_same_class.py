#!/usr/bin/python3
"""
    This module returns true or false
"""

def is_same_class(obj, a_class):
    """
        This function determines if
        an instance obj is of 'a_class' class
        using isinstance method
    """

    return isinstance(obj, a_class)
#!/usr/bin/python3
""" This module deal with json representation """


def class_to_json(obj):
    """
        This function converts python object
        to json object and returns it to a string
    """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res

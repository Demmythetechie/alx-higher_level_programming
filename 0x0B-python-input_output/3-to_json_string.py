#!/usr/bin/python3
"""This module deals with json representation"""
import json


def to_json_string(my_obj):
    """
        This converts python object of list to json object
        using dumps which returns the json object as a string
    """

    return json.dumps(my_obj)

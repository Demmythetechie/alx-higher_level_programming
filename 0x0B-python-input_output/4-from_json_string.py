#!/usr/bin/python3
"""This module deals with json representation"""
import json


def from_json_string(my_str):
    """
        This function converts json object to a python object
        returning it to a string
    """

    return json.loads(my_str)

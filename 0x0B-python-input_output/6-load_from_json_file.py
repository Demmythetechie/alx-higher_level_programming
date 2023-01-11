#!/usr/bin/python3
import json
"""This module deals with both json and file modification"""


def load_from_json_file(filename):
    """
        This function converts json object to python object.
        Taking the python object from a file.
        The json object is returned to a string
    """

    with open(filename, encoding="utf-8") as f:
        st = f.read()
        return json.loads(st)

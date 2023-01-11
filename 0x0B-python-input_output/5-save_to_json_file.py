#!/usr/bin/python3
"""This module deals with json repesentation"""
import json


def save_to_json_file(my_obj, filename):
    """
        This function converts python object to json
        and then returns it to a file
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

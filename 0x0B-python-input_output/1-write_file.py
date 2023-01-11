#!/usr/bin/python3
""" This module modifies a file """


def write_file(filename="", text=""):
    """
        This functions write a text to a file.
        If the file is not created it automatically
        creates it else it overwrite if it exist
    """

    with open(filename, 'w+', encoding="utf-8") as f:
        return f.write(text)

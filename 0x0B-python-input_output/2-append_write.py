#!/usr/bin/python3
""" This module modifies files """


def append_write(filename="", text=""):
    """
         This functions write a text to a file.
         If the file exist it automatically adds
         any text being inputed to the end of thr file
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

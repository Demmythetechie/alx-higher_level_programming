#/usr/bin/python3
"""
    This module modifies files
"""

def read_file(filename=""):
    """
        This function reads the content in the textfile
        and prints it out to standard output
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')

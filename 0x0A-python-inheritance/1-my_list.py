#!/usr/bin/python3
"""
    This class inherits the superclass list
    which is an inbuilt data type
"""


class MyList(list):
    """
        This class inherit and appends integers to an object of
        this class
    """

    def print_sorted(self):
        """
            This method sorts the instance of this class
        """
        self = sorted(self)
        print(self)

#!/usr/bin/python3
"""This module deals with inheritance"""


class MyInt(int):
    """This class inhetrits int"""

    def __eq__(self, other):
        """
            This method has been altered to give a
            function of '!=' instead of '=='
        """

        boo = True
        if self > other or self < other:
            boo = True
        else:
            boo = False
        return boo

    def __ne__(self, other):
        """
            This method has been altered to give a
            function of '==' instead of '!='
        """
        
        boo = True
        if self > other or self < other:
            boo = False
        else:
            boo = True
        return boo

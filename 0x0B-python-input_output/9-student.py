#!/usr/bin/python3
"""
    This module deals with conversion of
    custom python object to json object
"""
import json


class Student:
    """
        This converts the instance attribute
        of the class to json object
    """

    def __init__(self, first_name, last_name, age):
        """
            This method instantiate three attributes:
            first_name, last_name, age

            Args:
                first_name (string): students first name
                last_name (string): students last name
                age (int): students age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """conversion of init attribute takes place here"""
        
        return self.__dict__.copy()

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

    def to_json(self, attrs=None):
        """conversion of init attribute takes place here"""
        if attrs == None:
            attrs = ['age', 'first_name', 'last_name']
        js = {}
        if 'age' in attrs:
            js['age'] = self.age
        if 'last_name' in attrs:
            js['last_name'] = self.last_name
        if 'first_name' in attrs:
            js['first_name'] = self.first_name
        return js

    def __str__(self):
        return self.to_json()

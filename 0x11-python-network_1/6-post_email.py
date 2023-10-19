#!/usr/bin/python3
"""
This script takes in Url and sends a post request
to the pass Url with the parameter variable
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    This script takes in Url and sends a post request
    to the pass Url with the parameter variable
    """

    response = requests.post(argv[1], data={'email': argv[2]})
    print("{}".format(response.text))

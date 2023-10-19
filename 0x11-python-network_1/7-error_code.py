#!/usr/bin/python3
"""
This script takes in a url and sends a request
to the url and displays the body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    This script takes in a url and sends a request
    to the url and displays the body of the response
    """

    response = None
    try:
        response = requests.get(argv[1])
        print(response.text)
    except:
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))

#!/usr/bin/python3
"""
This py script takes in URL and sends a request to
displays the value of the variable X-Request-Id
in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    This py script takes in URL and sends a request to
    displays the value of the variable X-Request-Id
    in the response header
    """

    response = requests.get(argv[1])
    value = response.headers['X-Request-Id']
    print(value)

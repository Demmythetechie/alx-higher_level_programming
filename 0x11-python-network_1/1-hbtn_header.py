#!/usr/bin/python3
"""
This script takes sends a request to a
url and get the value to the variable
X-Request-Id
"""
from sys import argv
from urllib.request import urlopen


if __name__ == "__main__":
    """
    This script takes sends a request to a
    url and get the value to the variable
    X-Request-Id
    """

    with urlopen(argv[1]) as response:
        data = response.info()
    print(data.get('X-Request-Id'))

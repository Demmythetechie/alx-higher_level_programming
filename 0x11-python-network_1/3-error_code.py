#!/usr/bin/python3
"""
This script sends a request to a URL
and displays the body ofthe response
"""
from urllib.request import urlopen, Request
from sys import argv
import urllib.error as error


if __name__ == "__main__":
    """
    This script sends a request to a URL
    and displays the body ofthe response
    """

    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            data = response.read()
        print(data.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))

#!/usr/bin/python3
"""
This script takes in a url and
send a post request with a variable
email and also display the body response
"""
from urllib.request import Request, urlopen
import urllib.parse as parse
from sys import argv


if __name__ == "__main__":
    """
    This script takes in a url and
    send a post request with a variable
    email and also display the body response
    """
    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('utf-8')
    post = Request(argv[1], data)

    try:
        with urlopen(post) as response:
            data = response.read()
        print(data.decode('utf-8'))
    except:
        pass

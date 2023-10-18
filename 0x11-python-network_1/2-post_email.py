#!/usr/bin/python3
"""
This script takes in a url and
send a post request with a variable
email and also display the body response
"""
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    """
    This script takes in a url and
    send a post request with a variable
    email and also display the body response
    """

    post = Request(argv[1], headers={'email': argv[2]})
    try:
        with urlopen(post) as response:
            data = response.read()
        print(data.decode('utf-8'))
    except:
        pass

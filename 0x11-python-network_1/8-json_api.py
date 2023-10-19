#!/usr/bin/python3
"""
This script takes in a url and sends
a post request with the parameter 'q' with
or without a value
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    This script takes in a url and sends
    a post request with the parameter q with
    or without a value
    """

    if len(argv) <= 1:
        value = ""
    else:
        value = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': value})
    js = response.json()

    if type(js) == dict and len(js) != 0:
        print('[{}] {}'.format(js.get("id"), js.get("name")))
    elif type(js) != dict:
        print("Not a valid JSON")
    else:
        print("No result")

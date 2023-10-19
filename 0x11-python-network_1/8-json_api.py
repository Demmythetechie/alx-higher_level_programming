#!/usr/bin/python3
"""
This script takes in a url and sends
a post request with the parameter q
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    This script takes in a url and sends
    a post request with the parameter q
    """

    url = 'http://0.0.0.0:5000/search_user'
    if argv[1]:
        value = argv[1]
    else:
        value = ""

    response = requests.post(url, data={'q': value})
    js = response.json()
    if type(js) == dict and len(js) != 0:
        print('[{}] {}'.format(js.get("id"), js.get("name")))
    else if type(js) != dict:
        print("Not a valid JSON")
    else:
        print("No result")

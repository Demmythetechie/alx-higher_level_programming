#!/usr/bin/python3
"""
This script uses request to fetch data from the url
specified
"""
import requests


if __name__ == "__main__":
    """
    This script uses request to fetch data
    from the url specified
    """

    response = requests.get('https://alx-intranet.hbtn.io/status')

    print("""Body response:
\t- type: {}
\t- content: {}""".format(type(response.text), response.text), end='\n')

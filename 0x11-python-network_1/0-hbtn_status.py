#!/usr/bin/python3
"""
This py script fetches data from
https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen


if __name__ == "__main__":
    """
    Usage of urlopen along with "with" to get data
    from https://alx-intranet.hbtn.io/status
    """

    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        content = response.read()
        response.close()
    types = type(content)
    utf = content.decode('utf-8')
    print("""Body response:
- type: {}
- content: {}
- utf8 content: {}""".format(types, content, utf))

#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
using the requests package and displays the body of the response.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using urllib
and displays the body of the response in a formatted way.
"""

from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Use a with statement to handle the request and response
    with request.urlopen(url) as response:
        body = response.read()

        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))

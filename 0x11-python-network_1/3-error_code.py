#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the body
of the response (decoded in utf-8). It also handles HTTPError exceptions and
prints the error code when such an exception occurs.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

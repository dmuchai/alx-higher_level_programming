#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the value
of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a request to the URL and fetch the response
    with urllib.request.urlopen(url) as response:
        # Get the headers from the response
        headers = response.info()
        # Display the value of the X-Request-Id header
        print(headers.get("X-Request-Id"))

#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
- The letter must be sent in the variable q.
- If no argument is given, q is set to an empty string.
- If the response body is valid JSON and not empty, displays [<id>] <name>.
- Displays "Not a valid JSON" if the JSON is invalid.
- Displays "No result" if the JSON is empty.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": q}

    response = requests.post(url, data=data)
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(
                json_response.get("id"),
                json_response.get("name")
            ))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

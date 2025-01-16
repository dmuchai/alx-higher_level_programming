#!/bin/bash
#A script that sends a GET request to a URL and displays the body of the response only if the status code is 200
curl -Ls "$1"

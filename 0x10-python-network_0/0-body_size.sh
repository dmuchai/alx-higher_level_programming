#!/bin/bash
#A script that sends a request to a URL and displays the size of the body of the response in byte
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2

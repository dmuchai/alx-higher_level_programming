#!/bin/bash
# Sends a GET request to the URL with a custom header and displays the response body
curl -sH "X-School-User-Id: 98" "$1"

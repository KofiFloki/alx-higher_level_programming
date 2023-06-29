#!/bin/bash
# Take in URL as an argument, sends a GET request to the URL, and displays the body of the response as a header variable.
curl -s -H "X-School-User-Id":98 "$1"

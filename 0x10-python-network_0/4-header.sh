#!/usr/bin/bash
#this bash script takes in a URL as an argument, sends a GET request to the URL and displays the body of the response
#a header variable must be sent with the value 98
curl -sH "X-School-User-Id: 98" "$1"

#!/bin/bash
#send a request to a URL with a curl that displays the six=ze and body of the response
curl -s "$1" | wc -c

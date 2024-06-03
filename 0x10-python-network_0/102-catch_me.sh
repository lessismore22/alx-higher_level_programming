#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument and displays the body
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")"
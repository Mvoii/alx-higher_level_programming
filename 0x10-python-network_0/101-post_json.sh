#!/bin/bash
# sends a JSON POST request to a URL with given json file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

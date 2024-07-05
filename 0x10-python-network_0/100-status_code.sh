#!/bin/bash
# request to url passed as an argument, and display only the status code of the request
curl -s -o /dev/null -w "%{http_code}" "$1"

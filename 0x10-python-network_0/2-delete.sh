#!/bin/bash
# delete request passed as argument and displays the body of the response
curl -sX DELETE "$1"

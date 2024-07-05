#!/bin//bash
# displays all the HTTP methods the server will accept
curl -Is "$1" | grep Allow | cut -c 8-

#!/bin/bash
# makes a request to 0.0.0.0:5000catch_me that gets the response You got me!
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me

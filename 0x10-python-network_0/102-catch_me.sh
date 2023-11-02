#!/bin/bash
# Requests to 0.0.0.0:5000/catch_me that displays the message "You got me!"
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"

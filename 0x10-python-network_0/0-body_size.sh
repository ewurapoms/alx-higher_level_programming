#!/bin/bash
# Bash script that takes in a URL, sends it a request
# and prints the size of the body of the response
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2

#!/bin/bash
# takes in a URL and displays all HTTP methods the server accepts
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-

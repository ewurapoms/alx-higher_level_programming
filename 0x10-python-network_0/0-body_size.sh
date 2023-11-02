#!/bin/bash
# Bash script that takes in and sends request to URL 
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2

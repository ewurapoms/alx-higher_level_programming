#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email,
and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":

    path = sys.argv[1]
    output = requests.post(path, data={'email': sys.argv[2]})
    print(output.text)

#!/usr/bin/python3
"""
script takes in and sends a URL request, then displays
the value of the X-Request-Id variable found in the header
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as output:
        req = output.info()
        print(req.get('X-Request-Id'))

#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""

import sys
import requests


if __name__ == "__main__":

    query = requests.get(sys.argv[1])

    if 'X-Request-Id' in query.headers:
        output = query.headers['X-Request-Id']
        print(f"{output}")

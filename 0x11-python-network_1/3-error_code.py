#!/usr/bin/python3
"""
Script sends a request to URL and displays
body of the response while handling HTTP errors
"""

import sys
from urllib import error
from urllib import request


if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as output:
            print(output.read().decode('utf-8'))

    except error.HTTPError as fault:
        print('Error code: {}'.format(fault.code))

#!/usr/bin/python3
"""
script that takes in URL and email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

"""

import sys
import urllib.parse
import urllib.request
from urllib import request, parse


if __name__ == "__main__":
    attr = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(attr).encode("ascii")
    ask = request.Request(sys.argv[1], data)

    with request.urlopen(ask) as output:
        print(output.read().decode('utf-8'))

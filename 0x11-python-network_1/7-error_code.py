#!/usr/bin/python3
"""
 script that takes in a URL, sends a request to the URL
 and displays the body of the response
"""

import sys
import requests


if __name__ == "__main__":

    try:
        res = requests.get(sys.argv[1])
        res.raise_for_status()
        print(f"{res.text}")

    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(err.status_code))

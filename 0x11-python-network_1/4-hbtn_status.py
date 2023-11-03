#!/usr/bin/python3
"""script that retrieves URL with request packages"""

import requests


if __name__ == "__main__":

    query = requests.get('https://alx-intranet.hbtn.io/status')
    r = query.text

    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(r), r))

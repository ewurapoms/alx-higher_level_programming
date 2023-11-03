#!/usr/bin/python3
"""
Script uses GitHub credentials (username and password)
and API to display user_id
"""

import sys
from requests import get
from requests import auth


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    result = get(url, auth=auth.HTTPBasicAuth(username, password))
    print(result.json().get('id'))

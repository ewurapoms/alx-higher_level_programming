#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status
with urllib """

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

if __name__ == '__main__':

    with urllib.request.urlopen(url) as answer:
        output = answer.read()
        print("Body response:")
        print("\t- type: {}".format(type(output)))
        print("\t- content: {}".format(output))
        print("\t- utf8 content: {}".format(output.decode('utf-8')))

#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an object to a text file
    by a JSON representation"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)

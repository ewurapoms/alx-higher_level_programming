#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """ Function prints the JSON representation of an object

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded

    Returns:
        The JSON representation of a string object
    """
    return json.dumps(my_obj)

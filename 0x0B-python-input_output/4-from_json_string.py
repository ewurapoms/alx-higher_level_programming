#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Function that returns an object by a JSON representation"""
    return json.loads(my_str)

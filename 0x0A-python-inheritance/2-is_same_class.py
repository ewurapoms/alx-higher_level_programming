#!/usr/bin/python3
"""Defines a function of exact class."""


def is_same_class(obj, a_class):
    """Check if an object is the same as a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj
    Returns:
        If obj is exactly an instance of a_class - True.
        Else - False.
    """
    return True if type(obj) == a_class else False

#!/usr/bin/python3
"""Declares a locked class"""


class LockedClass:
    """
    Initializes LockedClass attributes
    for only attributes declared as 'first_name'.
    """

    __slots__ = ["first_name"]

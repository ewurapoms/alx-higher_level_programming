#!/usr/bin/python3
"""Defines a function that adds two integers"""


def add_integer(a, b=98):
    """ Function that adds two integers and/or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of the two given numbers

    Raises:
        TypeError: If neither 'a' nor 'b' are integers and/or float numbers

    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

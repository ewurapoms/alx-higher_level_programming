#!/usr/bin/python3
"""Declaration for function that prints a square"""


def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size of the square to print

    Raises:
        TypeError: If size is not an int


    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for num in range(size):
        print("#" * size)

#!/usr/bin/python3
"""Represents a peak finder in a list of unsorted integers"""


def find_peak(list_of_integers):
    """function finds peak in a list of integers"""

    if not list_of_integers:
        return None

    up = 0
    down = len(list_of_integers) - 1

    while up < down:
        middle = (up + down) // 2

        if list_of_integers[middle] < list_of_integers[middle + 1]:
            up = 1 + middle
        else:
            down = middle

    return list_of_integers[up]

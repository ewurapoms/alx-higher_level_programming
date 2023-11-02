#!/usr/bin/python3
"""Represents a peak finder in a list of unsorted integers"""


def find_peak(list_of_integers):
    """function finds peak in a list of integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    down = 0
    up = len(list_of_integers)
    center = ((up - down) // 2) + down
    center = int(center)
    if up == 1:
        return list_of_integers[0]
    if up == 2:
        return max(list_of_integers)
    if list_of_integers[center] >= list_of_integers[center - 1] and\
            list_of_integers[center] >= list_of_integers[center + 1]:
        return list_of_integers[center]
    if center > 0 and list_of_integers[center] < list_of_integers[center + 1]:
        return find_peak(list_of_integers[center:])
    if center > 0 and list_of_integers[center] < list_of_integers[center - 1]:
        return find_peak(list_of_integers[:center])

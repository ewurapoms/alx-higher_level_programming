#!/usr/bin/python3
""" Square definitions"""


class Square():
    """ Checks the area of a 'Square'
    """
    def __init__(self, size=0):
        """ prints a square instance """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ defines the square area """
        return self.__size ** 2

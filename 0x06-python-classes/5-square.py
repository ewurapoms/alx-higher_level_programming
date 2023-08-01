#!/usr/bin/python3
""" defines a class named Square """


class Square():
    """ Declaration of a 'Square'
    """
    def __init__(self, size=0):
        """ Initiation of a 'Square'
        """
        self.size = size

    @property
    def size(self):
        """ Finds the size of a square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ shows square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculate the area of a 'Square'
        """
        return self.size ** 2

    def my_print(self):
        """ Prints a visual of a square
        """
        print('\n'.join(['#' * self.size] * self.size))

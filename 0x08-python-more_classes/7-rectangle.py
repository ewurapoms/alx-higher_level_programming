#!/usr/bin/python3
""" Defines a class rectangle
"""


class Rectangle():
    """ Defines of a class to represent a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Instantiate a rectangle
        """
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    def __del__(self):
        """ Delete a rectangle
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """ Represent a rectangle as a string
        """
        if self.height and self.width:
            return '\n'.join(
                [str(self.print_symbol) * self.width] * self.height
            )
        return ''

    def __repr__(self):
        """ Represent a rectangle in a form that may be reused as input
        """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    @property
    def width(self):
        """ Get the width of a rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """  height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height of a rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Get the area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """ Get the perimeter of a rectangle
        """
        if self.width and self.height:
            return 2 * (self.width + self.height)
        return 0

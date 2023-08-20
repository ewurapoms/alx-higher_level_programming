#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle class

    Args:
        width(int): square's width
        height(int): square's height

    Attributes:
        __width: represents the private att
        __height: rep private att
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle"""
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """sets rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """sets rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """sets x value"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """sets y value"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() rep of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def display(self):
        """Prints a square with the `#` character."""
        for s in range(self.__y):
            print("")
        for h in range(1, self.__height+1):
            for a in range(self.__x):
                print(" ", end='')
            for pe in range(0, self.__width):
                print("#", end='')
            print("")

    def update(self, *args, **kwargs):
        """updates prev definitions"""
        listAtrbs = ["id", "_Rect_width", "_Rect_height", "_Rect_x", "_Rect_y"]
        ele = 0
        for arg in args:
            if ele == len(listAtrbs):
                break
            setattr(self, listAtrbs[ele], arg)
            ele = ele + 1
        if ele == 0:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        """displays dictionary"""
        return {'x': self.__x, 'y': self.__y,
                'id': self.id, 'height': self.__height, 'width': self.__width}

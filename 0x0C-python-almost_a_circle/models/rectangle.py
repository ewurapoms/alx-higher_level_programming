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
        """
        Args:
        *args (int): new arguments assigned to attributes
            1st argument = id attribute
            2nd argument = width attribute
            3rd argument = height attribute
            4th argument = x attribute
            5th argument = y attribute
        **kwargs (dict): key/value pairs of attributes
        """
        if args and len(args) != 0:
            attr = 0
            for arg in args:
                if attr == 0:
                    self.id = arg
                elif attr == 1:
                    self.width = arg
                elif attr == 2:
                    self.height = arg
                elif attr == 3:
                    self.x = arg
                elif attr == 4:
                    self.y = arg
                attr += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """displays dictionary"""
        return {'x': self.__x, 'y': self.__y,
                'id': self.id, 'height': self.__height, 'width': self.__width}

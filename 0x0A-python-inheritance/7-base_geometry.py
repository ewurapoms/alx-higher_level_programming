#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """rep base geometry"""

    def area(self):
        """ is empty"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        instance that validates an int
        Args:
            name (str): parameter name
            value (int): input value
        Raises:
            TypeError: where value isn't an integer.
            ValueError: where value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
""" Checks if object belongs with a class """


def is_kind_of_class(obj, a_class):
    """ Checks for object type if a_class or subclass of a_class
    """
    if isinstance(obj, a_class):
        return True
    return False

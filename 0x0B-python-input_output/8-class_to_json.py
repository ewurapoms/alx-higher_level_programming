#!/usr/bin/python3
"""Defines a class-to-JSON function."""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """
    return obj.__dict__

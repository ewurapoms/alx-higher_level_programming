#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """ Class that defines student instances """

    def __init__(self, first_name, last_name, age):
        """ function instantiates student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ method retrieves a dict rep of student instance """
        return self.__dict__.copy()

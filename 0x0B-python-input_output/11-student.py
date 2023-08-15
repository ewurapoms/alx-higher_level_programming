#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """ Class that defines student instances """

    def __init__(self, first_name, last_name, age):
        """ function instantiates student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ method retrieves a dict rep of student instance """
        if (type(attrs) == list and
                all(type(li) == str for li in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        for key, val in json.items():
            setattr(self, key, val)

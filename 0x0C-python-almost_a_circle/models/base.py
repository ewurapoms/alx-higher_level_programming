#!/usr/bin/python3
""" Defines a Class Base """

import json


class Base:
    """Displays a Base class

    Attributes:
        __nb_objects(int): private
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id: public attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON serialization of a list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json rep to file"""
        dictList = []
        for cases in list_objs:
            dictList.append(cases.to_dictionary())
        info = cls.to_json_string(dictList)
        filename = cls.__name__ + ".json"
        with open(filename, 'w+') as f:
            f.write(info)

    @staticmethod
    def from_json_string(json_string):
        """Displays the deserialization of a JSON string

        Returns:
            If json_string is None or empty, an empty list
            Otherwise - list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        temp = cls(1, 1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Creates a list from json_str"""
        json_str = ""
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f:
                json_str = f.read()
        except Exception:
            return []
        dictList = cls.from_json_string(json_str)
        cases = []
        for i in dictList:
            cases.append(cls.create(**i))
        return cases

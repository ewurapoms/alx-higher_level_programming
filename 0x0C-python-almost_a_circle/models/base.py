#!/usr/bin/python3
""" Defines a Class Base """

import json
import csv
import turtle


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
        filename = str(cls.__name__) + ".json"

        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_list = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(json_list))

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
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = None

        dummy.update(**dictionary)
        return dummy

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves CSV rep of list_objs to <class-name>.json"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                wprint = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    wprint.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Prints new class instances from a CSV file

        Returns:
            If the file does not exist - an empty list
            Otherwise - a list of instantiated classes
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dictList = csv.DictReader(csvfile, fieldnames=fieldnames)
                dictList = [dict([key, int(val)] for key, val in d.items())
                            for d in dictList]
                return [cls.create(**d) for d in dictList]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Shows a window that can draw all the Rectangles and Squares"""
        turtle.Screen().screensize(800, 600)
        turtle.Screen().title("Turtle Drawing")
        turtle.speed(1)
        turtle.bgcolor("FFFF00")
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        turt = turtle.Turtle()

        for rectangle in list_rectangles:
            turt.penup()
            turt.goto(rectangle.x, rectangle.y)
            turt.pendown()
            turt.color("#0000FF")
            for _ in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)

        for square in list_squares:
            turt.penup()
            turt.goto(square.x, square.y)
            turt.pendown()
            turt.color("#008000")
            for _ in range(4):
                turt.forward(square.width)
                turt.left(90)
                turt.hideturtle()

        screen.exitonclick()

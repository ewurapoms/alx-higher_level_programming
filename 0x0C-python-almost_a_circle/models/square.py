#!/usr/bin/python3
"""Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """sets the size"""
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """updates prev square info"""
        listAtrbs = ["id", "width", "height", "x", "y"]
        ele = 0
        for arg in args:
            if ele == len(listAtrbs):
                break
            if ele == 1:
                setattr(self, listAtrbs[ele], arg)
                setattr(self, listAtrbs[2], arg)
                ele += 1
            else:
                setattr(self, listAtrbs[ele], arg)
            ele += 1
        if ele == 0:
            for key, val in kwargs.items():
                if key == "size":
                    setattr(self, "width", val)
                    setattr(self, "height", val)
                elif hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        """defines a dict"""
        return {'x': self.x, 'y': self.y,
                'id': self.id, 'size': self.height}

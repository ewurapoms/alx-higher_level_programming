#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append

    """
    text = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for row in f:
            text = text + row
            if search_string in row:
                text += new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

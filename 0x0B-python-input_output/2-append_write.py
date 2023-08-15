#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """ function that appends to a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """ function writes to a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    Returns:
        The number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

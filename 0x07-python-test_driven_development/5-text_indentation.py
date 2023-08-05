#!/usr/bin/python3
"""Defines a 'text_indentation' function that formats text"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in '.:?':
        text = text.replace(char, char + '\n\n')
    print(*(ti.strip() for ti in (text + '\n').splitlines()), sep='\n', end='')

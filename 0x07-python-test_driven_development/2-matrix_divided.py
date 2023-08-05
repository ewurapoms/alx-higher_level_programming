#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix

    Args:
        matrix: is the list of a lists of integers/floats
        div: is the divisor num

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix are not lists
                   If the elemetns of the lists doesn't have integers/floats
                   If div is not an integer/float num
                   If the lists of the matrix are of different sizes

        ZeroDivisionError: If div is zero(0)


    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msgDetails = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msgDetails)

    length = 0
    size_ = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(msgDetails)

        if length != 0 and len(elements) != length:
            raise TypeError(size_)

        for num in elements:
            if not type(num) in (int, float):
                raise TypeError(msgDetails)

        length = len(elements)

    mx = list(map(lambda a: list(map(lambda b: round(b / div, 2), a)), matrix))
    return (mx)

#!/usr/bin/python3
"""Defines a function that multiplies a matrix"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elements in m_a:
        if not isinstance(elements, list):
            raise TypeError("m_a must be a list of lists")

    for elements in m_b:
        if not isinstance(elements, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elements in lists:
            if not type(elements) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elements in lists:
            if not type(elements) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    length = 0

    for elements in m_a:
        if length != 0 and length != len(elements):
            raise TypeError("each row of m_a must be of the same size")
        length = len(elements)

    length = 0

    for elements in m_b:
        if length != 0 and length != len(elements):
            raise TypeError("each row of m_b must be of the same size")
        length = len(elements)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    index1 = 0

    for a in m_a:
        new_row = []
        index2 = 0
        num = 0
        while (index2 < len(m_b[0])):
            num += a[index1] * m_b[index1][index2]
            if index1 == len(m_b) - 1:
                index1 = 0
                index2 += 1
                new_row.append(num)
                num = 0
            else:
                index1 += 1
        new_matrix.append(new_row)

    return new_matrix

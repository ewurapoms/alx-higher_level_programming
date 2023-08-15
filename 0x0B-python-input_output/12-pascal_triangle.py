#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Displays Pascal's Triangle of size n

    Returns:
    list of num in triangle
    """
    if n < 1:
        return []

    pasc_tri = [[1]]
    while len(pasc_tri) != n:
        triangle = pasc_tri[-1]
        temp = [1]
        for num in range(len(triangle) - 1):
            temp.append(triangle[num] + triangle[num + 1])
        temp.append(1)
        pasc_tri.append(temp)
    return pasc_tri

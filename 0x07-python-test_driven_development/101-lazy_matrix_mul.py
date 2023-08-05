#!/usr/bin/python3
""" Defines a function that multiplies 2 matrices """

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        result of the multiplication

    """

    return (np.matmul(m_a, m_b))

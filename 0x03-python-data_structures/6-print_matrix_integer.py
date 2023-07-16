#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return (None)
    print('\n'.join([' '.join(['{:d}'.format(n) for n in x]) for x in matrix]))

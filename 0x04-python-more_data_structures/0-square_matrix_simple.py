#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        return [list(map(lambda x: x**2, elem)) for elem in matrix] 

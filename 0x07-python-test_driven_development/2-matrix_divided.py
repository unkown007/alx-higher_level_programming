#!/usr/bin/python3
"""Divide all elements of a matrix
Args:
    matrix(list): list compound of list of numbers
    div(int): integer number
"""


def matrix_divided(matrix, div):
    """Raises:
        TypeError: if the matrix have values diferent from integers or floats
        or the matrix rows with different sizes or div is not a number
        ZeroDivisionError: if div is equal to 0
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        new_row = []
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)
    return new_matrix

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for x in matrix:
            for i in range(0, len(x)):
                print("{:d}{}".format(
                        x[i],
                        " " if i < len(x) - 1 else ""), end="")
            print()

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        new_row = ["{:d}".format(no) for no in row]
        print(" ".join(new_row))

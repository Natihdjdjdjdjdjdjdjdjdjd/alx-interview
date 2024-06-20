#!/usr/bin/python3
"""
the module 2D Matrix transposition approach
"""


def rotate_2d_matrix(matrix):
    """ the function that rotates n x n 2D matrix in  90 decrease
    """
    matrix.reverse()
    d_len = len(matrix)
    for x in range(d_len):
        for y in range(x):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    matrix[:] = [[matrix[j][i] for j in range(n)][::-1] for i in range(n)]

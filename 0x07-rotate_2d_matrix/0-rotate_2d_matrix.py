#!/usr/bin/python3
"""
Rotate a 2D Matrix.
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix at 90 degrees clockwise
    Args:
        matrix (list[[list]]): the matrix
    """
    a = len(matrix)
    for i in range(int(a / 2)):
        m = (a - i - 1)
        for j in range(i, m):
            b = (a - 1 - j)
            # the current number
            tmp = matrix[i][j]
            # change top for left
            matrix[i][j] = matrix[b][i]
            # change left for bottom
            matrix[b][i] = matrix[m][b]
            # change bottom for right
            matrix[m][b] = matrix[j][m]
            # change right for top
            matrix[j][m] = tmp

#!/usr/bin/python3
"""
Generate Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    :param n: An integer representing the number of rows in Pascal's Triangle.
    :return: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle

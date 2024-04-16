#!/usr/bin/env python3

"""Pascals triangle"""

def pascal_triangle(n):
    """
    returns a list of lists representing the pascal triangle
    returns an empty list if n <= 0
    n must always be an integer
    Args:
        n (integer): number of rows in the pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    if n == 0:
        return [[1]]

    triangle = [[1]]
    for i in range(n-1):
        triangle.append([a+b for a, b in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
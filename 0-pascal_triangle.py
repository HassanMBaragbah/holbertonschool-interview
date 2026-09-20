#!/usr/bin/python3
"""Module that defines the pascal_triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]

        for j in range(len(prev_row) - 1):
            current_row.append(prev_row[j] + prev_row[j + 1])

        current_row.append(1)
        triangle.append(current_row)

    return triangle

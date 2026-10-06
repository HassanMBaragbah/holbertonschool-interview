#!/usr/bin/python3
"""
Module to calculate the minimum number of operations
to achieve n 'H' characters in a text file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n 'H' characters in the file.
    Args:
        n (int): Target number of 'H' characters.
    Returns:
        int: Minimum number of operations, or 0 if n <= 1.
    """
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations

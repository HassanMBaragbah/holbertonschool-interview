#!/usr/bin/python3
"""
Module that validates whether a given data
set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list of int): List of integers representing bytes.
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        byte = num & 0xFF

        if n_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            if n_bytes == 1 or n_bytes > 4:
                return False

            if n_bytes == 0:
                continue

            n_bytes -= 1
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            n_bytes -= 1

    return n_bytes == 0

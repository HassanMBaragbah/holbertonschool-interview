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

    # Masks for checking bit patterns
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Check if the integer exceeds a single byte range (0-255)
        if num < 0 or num > 255:
            return False

        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1s to
            # find character length (1 to 4 bytes)
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            # 1-byte characters (ASCII) have 0 leading bytes (n_bytes == 0)
            # Invalid lengths: 1-byte indicator is impossible, > 4 is invalid
            if n_bytes == 1 or n_bytes > 4:
                return False

            if n_bytes == 0:
                continue

            # Decrement to account for the current starting byte
            n_bytes -= 1
        else:
            # Continuation bytes must start with '10' (1st bit 1, 2nd bit 0)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            n_bytes -= 1

    return n_bytes == 0

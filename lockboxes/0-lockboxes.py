#!/usr/bin/env python3
"""
Module to determine if all locked boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): A list where each element is a list
                                     of keys contained in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    unlocked = set([0])
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == n
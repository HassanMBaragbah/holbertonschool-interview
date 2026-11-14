#!/usr/bin/python3
"""
Module for solving the coin change problem.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): The values of the coins in possession.
        total (int): The target amount to reach.

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if impossible.
    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    # Initialize DP array where dp[i] is the min coins needed for amount i.
    # Use total + 1 (an unreachable upper bound) as a placeholder for infinity.
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Sort coins to allow early exit in the inner loop
    coins.sort()

    for i in range(1, total + 1):
        for coin in coins:
            if coin > i:
                break
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[total] if dp[total] <= total else -1

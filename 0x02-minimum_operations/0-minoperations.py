#!/usr/bin/python3
""" Module of 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets the fewest # of operations needed to result in exactly n H chars
    """
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops

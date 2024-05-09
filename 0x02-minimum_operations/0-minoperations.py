#!/usr/bin/python3
"""
Minimum operations  the fewest number of operations needed to result
    in exactly n H characters
"""


def minOperations(n):
    """
    n a text file, there is a single character H.a
    """
    if n <= 1:
        return 0
    for j in range(2, n+1):
        if n % j == 0:
            return minOperations(int(n/j)) + j

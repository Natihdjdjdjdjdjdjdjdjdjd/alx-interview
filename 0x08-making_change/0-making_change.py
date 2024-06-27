#!/usr/bin/python3

""" the function Contains makeChange function"""


def makeChange(coins, total):
    """
    the modulue that trie to Returnsfewest number of coins needed to meet tot
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    my_change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            my_change += 1
        if (total == 0):
            return my_change
    return -1

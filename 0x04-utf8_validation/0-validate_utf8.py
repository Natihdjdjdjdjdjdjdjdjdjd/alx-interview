#!/usr/bin/python3
"""
the module that help for UTF-8 Validation
"""


def validUTF8(data):
    """
    data: a list of integers
    """
    b_count = 0

    for x in data:
        if b_count == 0:
            if x >> 5 == 0b110 or x >> 5 == 0b1110:
                b_count = 1
            elif x >> 4 == 0b1110:
                b_count = 2
            elif x >> 3 == 0b11110:
                b__count = 3
            elif x >> 7 == 0b1:
                return False
        else:
            if x >> 6 != 0b10:
                return False
            b_count -= 1
    return b_count == 0

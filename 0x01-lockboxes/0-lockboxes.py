#!/usr/bin/python3
"""the module that help toboxes open"""


def canUnlockAll(boxes):
    """helps to let the boxes can be opened"""
    if (type(boxes) is not list or len(boxes) == 0):
        return False
    for x in range(1, len(boxes) - 1):
        unlocked = False
        for i in range(len(boxes)):
            unlocked = y in boxes[i] and x != i
            if unlocked:
                break
        if unlocked is False:
            return unlocked
    return True

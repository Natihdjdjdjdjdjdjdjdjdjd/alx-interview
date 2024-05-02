#!/usr/bin/python3
"""
This is a module that provides a function for determining if all
boxes in a given list can be opened.
"""


def canUnlockAll(boxes):
    """
    let thw function takes a list of lists and returns a boolean indicating
        
    """
    m = len(boxes)
    let_seen_boxes = set([0])
    let_unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(let_unseen_boxes) > 0:
        boxIdx = let_unseen_boxes.pop()
        if not boxIdx or boxIdx >= m or boxIdx < 0:
            continue
        if boxIdx not in let_seen_boxes:
            let_unseen_boxes = let_unseen_boxes.union(boxes[boxIdx])
            let_seen_boxes.add(boxIdx)
    return m == len(let_seen_boxes)

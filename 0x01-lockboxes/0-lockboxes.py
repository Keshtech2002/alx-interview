#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    -  all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    canUnlockAll = False
    keys = {0: True}
    n_boxes = len(boxes)
    while (True):

        n_keys = len(keys)

        for x in range(len(boxes)):
            if boxes[x] and keys.get(x, False):
                for y in boxes[x]:
                    if y < n_boxes:
                        keys[y] = True
                    boxes[x] = None

        if not (len(keys) > n_keys):
            break

    if n_keys == len(boxes):
        canUnlockAll = True

    return canUnlockAll

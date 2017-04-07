import sys


def contains(a, b):
    """
    returns 1 if a is smaller than b
    else, returns 2
    """
    if a[0] > b[0] and a[1] > b[1]: return 1
    if a[1] > b[0] and a[0] > b[1]: return 1
    return 0


def load()
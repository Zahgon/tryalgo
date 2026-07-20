#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def subset_sum(x, R):
    pass


def coin_change(x, R):
    """Coin change

    :param x: table of non negative values
    :param R: target value
    :returns bool: True if there is a non negative linear combination
        of x that has value R
    :complexity: O(n*R)
    """
    b = [False] * (R + 1)
    b[0] = True
    for xi in x:
        for s in range(xi, R + 1):
            b[s] |= b[s - xi]
    return b[R]

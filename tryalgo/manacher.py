#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def manacher(s):
    """Longest palindrome in a string by Manacher

    :param s: string
    :requires: s is not empty
    :returns: i,j such that s[i:j] is the longest palindrome in s
    :complexity: O(len(s))
    """
    assert set.isdisjoint({'$', '^', '#'}, s)  # Forbidden letters
    if s == "":
        return (0, 0)           # returns indices of empty string
    t = "^#" + "#".join(s) + "#$"
    c = 1
    d = 1
    p = [0] * len(t)
    for i in range(2, len(t) - 1):
        mirror = 2 * c - i         # = c - (i-c)
        p[i] = max(0, min(d - i, p[mirror]))
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > d:
            c = i
            d = i + p[i]
    (k, i) = max((p[i], i) for i in range(1, len(t) - 1))
    return ((i - k) // 2, (i + k) // 2)  # extract solution

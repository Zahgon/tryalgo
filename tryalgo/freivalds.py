#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from sys import stdin

__all__ = ["freivalds"]


def readint():
    """
    function to read an integer from stdin
    """
    return int(stdin.readline())


def readarray(typ):
    """
    function to read an array
    """
    return list(map(typ, stdin.readline().split()))


def readmatrix(n):
    """
    function to read a matrix
    """
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M


def mult(M, v):
    """
    function to multiply a matrix times a vector
    """
    n = len(M)
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]


def freivalds(A, B, C):
    """Tests matrix product AB=C by Freivalds

    :param A: n by n numerical matrix
    :param B: same
    :param C: same
    :returns: False with high probability if AB != C

    :complexity:
        :math:`O(n^2)`
    """
    n = len(A)
    x = [randint(0, 1000000) for j in range(n)]
    return mult(A, mult(B, x)) == mult(C, x)


if __name__ == "__main__":
    n = readint()
    A = readmatrix(n)
    B = readmatrix(n)
    C = readmatrix(n)
    print(freivalds(A, B, C))

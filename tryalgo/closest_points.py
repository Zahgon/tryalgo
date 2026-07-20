#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import randint


from math import hypot   # hypot(dx, dy) = sqrt(dx * dx + dy * dy)
from math import floor
from random import shuffle

__all__ = ["closest_points"]


def dist(p, q):
    return hypot(p[0] - q[0], p[1] - q[1])  # Euclidean dist.


def cell(point, size):
    """ returns the grid cell coordinates containing the given point.
    
    :param point: couple of coordinates
    :param size: floating point number, side length of a grid cell
    """
    x, y = point                        
    return (floor(x / size), floor(y / size))


def improve(S, d):
    G = {}                              # maps grid cell to its point
    for p in S:                         # for every point
        a, b = cell(p, d / 2)           # determine its grid cell
        for a1 in range(a - 2, a + 3):
            for b1 in range(b - 2, b + 3):
                if (a1, b1) in G:       # compare with points
                    q = G[a1, b1]       # in surrounding cells
                    pq = dist(p, q)
                    if pq < d:          # improvement found
                        return pq, p, q
        G[a, b] = p
    return None


def closest_points(S):
    """Closest pair of points

    :param S: list of points
    :requires: size of S at least 2
    :modifies: changes the order in S
    :returns: pair of points p,q from S with minimum Euclidean distance
    :complexity: expected linear time
    """
    shuffle(S)
    assert len(S) >= 2
    p = S[0]                # start with distance between
    q = S[1]                # first two points
    d = dist(p, q)
    while d > 0:            # distance 0 cannot be improved
        r = improve(S, d)
        if r:               # distance improved
            d, p, q = r
        else:               # r is None: could not improve
            break
    return p, q


if __name__ == "__main__":

    def tikz_points(S):
        pass

    def tikz_polygone(S):
        pass

    S = [(randint(0, 400) / 100, randint(0, 400) / 100) for _ in range(32)]
    tikz_points(S)
    tikz_polygone(closest_points(S))

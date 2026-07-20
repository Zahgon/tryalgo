#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tryalgo.range_minimum_query import RangeMinQuery


def area(p):
    """Area of a polygone

    :param p: list of the points taken in any orientation,
              p[0] can differ from p[-1]
    :returns: area
    :complexity: linear
    """
    A = 0
    for i, _ in enumerate(p):
        A += p[i - 1][0] * p[i][1] - p[i][0] * p[i - 1][1]
    return A / 2.


def is_simple(polygon):
    """Test if a rectilinear polygon is is_simple

    :param polygon: list of points as (x,y) pairs along the closed polygon
    :returns: True if the segements do not intersect
    :complexity: O(n log n) for n=len(polygon)
    """
    n = len(polygon)
    order = list(range(n))
    order.sort(key=lambda i: polygon[i])         # lexicographic order
    rank_to_y = list(set(p[1] for p in polygon))
    rank_to_y.sort()
    y_to_rank = {y: rank for rank, y in enumerate(rank_to_y)}
    S = RangeMinQuery([0] * len(rank_to_y))      # sweep structure
    last_y = None
    for i in order:
        x, y = polygon[i]
        rank = y_to_rank[y]
        right_x = max(polygon[i - 1][0], polygon[(i + 1) % n][0])
        left = x < right_x
        below_y = min(polygon[i - 1][1], polygon[(i + 1) % n][1])
        high = y > below_y
        if left:                      # y does not need to be in S yet
            if S[rank]:
                return False          # two horizontal segments intersect
            S[rank] = -1              # add y to S
        else:
            S[rank] = 0               # remove y from S
        if high:
            lo = y_to_rank[below_y]   # check S between [lo + 1, rank - 1]
            if (below_y != last_y or last_y == y or
                    rank - lo >= 2 and S.range_min(lo + 1, rank)):
                return False          # horiz. & vert. segments intersect
        last_y = y                    # remember for next iteration
    return True








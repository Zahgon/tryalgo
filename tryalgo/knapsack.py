#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def knapsack(p, v, cmax):
    """Knapsack problem: select maximum value set of items if total size not
    more than capacity

    :param p: table with size of items
    :param v: table with value of items
    :param cmax: capacity of bag
    :requires: number of items non-zero
    :returns: value optimal solution, list of item indexes in solution
    :complexity: O(n * cmax), for n = number of items
    """
    n = len(p)
    opt = [[0] * (cmax + 1) for _ in range(n + 1)]
    sel = [[False] * (cmax + 1) for _ in range(n + 1)]
    for cap in range(p[0], cmax + 1):
        opt[0][cap] = v[0]
        sel[0][cap] = True
    for i in range(1, n):
        for cap in range(cmax + 1):
            if cap >= p[i] and opt[i-1][cap - p[i]] + v[i] > opt[i-1][cap]:
                opt[i][cap] = opt[i-1][cap - p[i]] + v[i]
                sel[i][cap] = True
            else:
                opt[i][cap] = opt[i-1][cap]
                sel[i][cap] = False
    cap = cmax
    solution = []
    for i in range(n-1, -1, -1):
        if sel[i][cap]:
            solution.append(i)
            cap -= p[i]
    return (opt[n - 1][cmax], solution)


def knapsack2(p, v, cmax):
    """Knapsack problem: select maximum value set of items if total size not
    more than capacity.
    alternative implementation with same behavior.

    :param p: table with size of items
    :param v: table with value of items
    :param cmax: capacity of bag
    :requires: number of items non-zero
    :returns: value optimal solution, list of item indexes in solution
    :complexity: O(n * cmax), for n = number of items
    """
    n = len(p)
    pgv = [[0] * (cmax + 1) for _ in range(n)]
    for c in range(cmax + 1):  # Initialisation
        pgv[0][c] = v[0] if c >= p[0] else 0
    pred = {}  # Prédécesseurs pour mémoriser les choix faits
    for i in range(1, n):
        for c in range(cmax + 1):
            pgv[i][c] = pgv[i - 1][c]  # Si on ne prend pas l'objet i
            pred[(i, c)] = (i - 1, c)
            if c >= p[i] and pgv[i - 1][c - p[i]] + v[i] > pgv[i][c]:
                pgv[i][c] = pgv[i - 1][c - p[i]] + v[i]
                pred[(i, c)] = (i - 1, c - p[i])  # On marque le prédécesseur
    cursor = (n - 1, cmax)
    chosen = []
    while cursor in pred:
        if pred[cursor][1] < cursor[1]:
            chosen.append(cursor[0])
        cursor = pred[cursor]
    if cursor[1] > 0:  # A-t-on pris le premier objet ?
        chosen.append(cursor[0])
    return pgv[n - 1][cmax], chosen

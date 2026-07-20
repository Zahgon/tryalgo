#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys


def read(filename):
    pass


def horn_sat(formula):
    """ Solving a HORN Sat formula

    :param formula: list of couple(posvar, negvars).
                    negvars is a list of the negative variables (can be empty)
                    posvar is the positive variable (can be None)
                    Variables can be any hashable objects: integers, strings...
    :returns: None if formula is not satisfiable, else a minimal set of vars
              that have to be set to true in order to satisfy the formula.
    :complexity: linear
    """
    CLAUSES = range(len(formula))
    score = [0 for c in CLAUSES]  # number of neg vars not yet in solution
    posvar_in_clause = [None for c in CLAUSES]
    clauses_with_negvar = defaultdict(set)
    for c in CLAUSES:
        posvar, negvars = formula[c]
        score[c] = len(set(negvars))  # do not count twice negative variables
        posvar_in_clause[c] = posvar
        for v in negvars:
            clauses_with_negvar[v].add(c)
    pool = [set() for s in range(max(score) + 1)]   # create the pool
    for c in CLAUSES:
        pool[score[c]].add(c)           # pool[s] = set of clauses with score s

    solution = set()                    # contains all variables set to True
    while pool[0]:
        curr = pool[0].pop()               # arbitrary zero score clause
        v = posvar_in_clause[curr]
        if v is None:                      # formula is not satisfiable
            return None
        if v in solution or curr in clauses_with_negvar[v]:
            continue                       # clause is already satisfied
        solution.add(v)
        for c in clauses_with_negvar[v]:   # update score
            pool[score[c]].remove(c)
            score[c] -= 1
            pool[score[c]].add(c)          # change c to lower score in pool
    return solution


if __name__ == "__main__":
    F = read(sys.argv[1])
    sol = horn_sat(F)
    if sol is None:
        print("No solution")
    else:
        print("Minimal solution:")
        for x in sorted(sol):
            print(x)

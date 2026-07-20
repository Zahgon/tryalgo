#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def tortoise_hare(f, source=0):
    """ Detect cycle for function f, starting from source

    :param f: function from finite domain to itself
    :param source: element in this domain
    :warning: if the function does not reach a cycle from source
              then this function loops forever
    :returns: c, d such that after d iterations 
              of f a cycle is reached, which has period c
    :complexity: `O(d+c)`
    """
    t = f(source)       # tortoise
    h = f(f(source))    # hare

    while t != h:
        t = f(t)
        h = f(f(h))
    t = source
    d = 0
    while t != h:
        t = f(t)
        h = f(h)
        d += 1
    c = 1
    t = f(t)
    while t != h:
        t = f(t)
        c += 1
    return c, d



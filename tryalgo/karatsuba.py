#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def eval_poly(P, x):
    pass

def add_poly(P, Q):
    """ Add two polynomials represented by their coefficients.
    :param P, Q: two vectors representing polynomials
    :returns: a vector representing the addition
    :complexity: linear in the size of P and Q.
    """
    if len(P) < len(Q):
        P, Q = Q, P     # add the shorter to the longer vector
    R = P[::]           # make a copy
    for i, qi in enumerate(Q):
        R[i] += qi      # cumulate Q into R
    return R 

def sub_poly(P, Q):
    """ Subtruct two polynomials represented by their coefficients.
    :param P, Q: two vectrs representing polynomials
    :returns: a vector representing the difference
    :complexity: linear in the size of P and Q.
    """
    return add_poly(P, [-qi for qi in Q])

def mul_poly(P, Q):                   
    """ Karatsuba's algorithm. 
    Multiply two polynomials represented by their coefficients.
    i.e. P(x) = sum P[i] x**i.
    :param P, Q: two vectors representing polynomials
    :returns: a vector representing the product
    :complexity: $O(n^{\log_2 3})=O(n^{1.585})$, where n is total degree of P and Q.
    """
    if not P or not Q:  # case one of P, Q is the constant zero
        return []
    if len(P) == 1:
        return [qi * P[0] for qi in Q]
    elif len(Q) == 1:
        return [pi * Q[0] for pi in P]
    k = max(len(P), len(Q)) // 2
    xk = [0] * k
    a = P[:k]           # split: P = a + b * x**k
    b = P[k:]
    c = Q[:k]           # split: Q = c + d * x**k
    d = Q[k:]
    a_b = sub_poly(a, b)
    c_d = sub_poly(c, d)
    ac = mul_poly(a, c)
    bd = mul_poly(b, d)
    abcd = mul_poly(a_b, c_d)
    ad_bc = sub_poly(add_poly(ac, bd), abcd)    # = ad - bc
    return add_poly(ac, xk + add_poly(ad_bc, xk + bd))

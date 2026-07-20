#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def part_sum(x_table, i=0):
    pass


def subset_sum(x_table, r_target):
    pass


def part_sum2(x_table):
    """All subsetsums from a list x

    :param x_table: list of values
    :complexity: :math:`O(2^{len(x)})`
    """
    answer = set([0])        # 0 = value of empty set
    for xi in x_table:
        answer |= set(value + xi for value in answer)
    return answer


def subset_sum2(x_table, r_target):
    """Subsetsum by splitting

    :param x_table: table of values
    :param r_target: target value
    :returns bool: if there is a subsequence of x_table with total sum r_target
    :complexity: :math:`O(n^{\\lceil n/2 \\rceil})`
    """
    k = len(x_table) // 2              # divide input
    y_set = part_sum2(x_table[:k])
    z_set = set(r_target - value for value in part_sum2(x_table[k:]))
    return len(y_set & z_set) > 0        # test intersection

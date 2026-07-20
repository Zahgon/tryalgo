#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ["predictive_text", "propose"]

t9 = "22233344455566677778889999"


def letter_to_digit(x):
    pass


def code_word(word):
    """:returns: the digit correspondence for given word"""
    return ''.join(map(letter_to_digit, word))


def predictive_text(dic):
    """Predictive text for mobile phones

    :param dic: associates weights to words from [a-z]*
    :returns: a dictionary associating to words from [2-9]*
             a corresponding word from the dictionary with highest weight
    :complexity: linear in total word length
    """
    total_weight = {}
    for word, weight in dic:
        prefix = ""
        for x in word:
            prefix += x
            if prefix in total_weight:
                total_weight[prefix] += weight
            else:
                total_weight[prefix] = weight
    prop = {}
    for prefix in total_weight:
        code = code_word(prefix)
        if (code not in prop
                or total_weight[prop[code]] < total_weight[prefix]):
            prop[code] = prefix
    return prop


def propose(prop, seq):
    """wrapper to access a dictionary even for non-present keys"""
    if seq in prop:
        return prop[seq]
    return None

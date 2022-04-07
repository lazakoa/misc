#!/bin/env python

"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""

import itertools
from functools import reduce

def form(i):
    """
        turns a iterable into a int
    """
    return int(reduce(lambda x,y: str(x) + str(y), i))

ans = itertools.permutations(range(10))

if __name__ == "__main__":
    n = 10**6 - 1 # ok wtf happened here? Got it now ... i'm a idiot
    print(form(next(itertools.islice(ans, n, None))))

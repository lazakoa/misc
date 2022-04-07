"""
Project Euler Problem 78
========================

Let p(n) represent the number of different ways in which n coins can 
be separated into piles. For example, five coins can separated into 
piles in exactly seven different ways, so p(5)=7.

                            OOOOO

                            OOOO   O

                            OOO   OO

                            OOO   O   O

                            OO   OO   O

                            OO   O   O   O

                            O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

# this is too slow.

"""
Need a faster variant of the above, need to find a different 
recurrence.
"""

# why is this giving me so much trouble :(, i know the solution.
from math import floor

def pentagonal(n):
    return (3*n*n - n) // 2

# Come back and finish later.

def pentagonalPool(k):
    """
        Calculates a large pool of pentagonal numbers. This is for
        generalized pentagonal numbers. 
    """
    pool = {0: 0}
    index = 1
    n = 1
    while True:
        pool[index] = pentagonal(n)
        index += 1
        pool[index] = pentagonal(-1*n)
        index += 1
        n += 1
        if n >= k:
            break
    return pool

pentCache = pentagonalPool(10**5)
partitionCache = {0: 1, 1: 1}

def partition(n):
    pass


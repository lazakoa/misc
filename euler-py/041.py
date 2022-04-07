"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

"""
    * generate all permutations that can be made with the digits 1 to n
    * keep cycling through values of n
    * as first approximation assume n ends at 9
    * primes have to end on a odd digit (1,3,5,7,9), ignore at first to make 
    things easier
"""

from itertools import permutations, chain
from prime import is_prime
from functools import reduce

def genPandigitalIterator(n):
    """
    An iterator that generates all of the pandigital numbers from 1 to n. Takes
    an interger n as an argument.
    """
    return map(lambda x: int(''.join(list(map(str, x))))
        , permutations(range(1, n+1)))

def primePandigitalIterator(n):
    """
    Returns a prime pandigital iterator.
    """

    return filter(is_prime, genPandigitalIterator(n))

def chainedPandigital(n):

    temp = primePandigitalIterator(1)

    for i in range(2, n+1):
        temp = chain(temp, primePandigitalIterator(i))

    return temp

print(reduce(lambda x,y: x if x > y else y, chainedPandigital(9)))


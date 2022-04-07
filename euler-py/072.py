"""
Project Euler Problem 72
========================

Consider the fraction, n/d, where n and d are positive integers. If 
n < d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending 
order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper
fractions for d 1,000,000?
"""

# 1/2
# 1/3, 2/3
# 1/4, 2/4, 3/4
# 1/5, 2/5, 3/5, 4/5
# 1/6, 2/6, 3/6, 4/6, 5/6
# 1/7, 2/7, 3/7, 4/7, 5/7, 6/7
# 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8

"""
    Eulers totient function lets me count how many numbers are 
    relatively prime to n, eg phi(n) = k where k is an integer.

    Properties of Eulers totient function to abuse:

    when n is prime:
    * phi(n) = n - 1

    when m and n are coprime:
    * phi(m*n) = phi(m)*phi(n)

    Find all the primes upto d, and factorize all the numbers up to
    d. Generate a dictionary of phi(prime) and use these values to
    build up all the euler totient functions.

    using eulerlib to do the heavy lifting for the factorization
"""

"""
    Scrap all of the above.

    F_n = (1/2)*(n+3)*n - Sum(d=2,n) F_(floor(n/d))

    Farey sequences and Mobius functions don't simplify this at all.

    Going to use numpy factorized functions for a speed up.
"""

import fractions
import numpy as np
import math


def Farey(n):

    cache = {8: 23, 100: 3045}

    def inner(n):
        if n == 1:
            return 2
        else:
            total = fractions.Fraction(1/2)*(n + 3)*n
            for i in range(2, n + 1):

                temp = int(math.floor(n/i))

                if temp in cache:
                    total = total - cache[temp]
                else:
                    cache[temp] = inner(temp)
                    total = total - cache[temp]
            return total

    return inner(n) - 2

print(Farey(10000))

"""
Project Euler Problem 77
========================

It is possible to write ten as the sum of primes in exactly five 
different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in 
over five thousand different ways?
"""

"""
    * given n, get a list of primes upto n
    * for each prime generate the polynomial
    * multiply all the polynomials together
    * and look for the corresponding factor
"""

import numpy as np
from eulerlib import primes
from functools import reduce

def PrimePartition(n):
    coeffs = primes(n)
    polynomials = []
    for prime in coeffs:
        poly = [1]
        while (len(poly) - 1) != n:
            if (len(poly)) % prime == 0:
                poly.append(1)
            else:
                poly.append(0)
        polynomials.append(poly)

    return reduce(lambda x, y: np.polymul(x, y), polynomials)[n]

"""
# Sanity check, works
print(PrimePartition(14))
"""
i = 10
while True:
    if PrimePartition(i) >= 5000:
        break
    else:
        i += 1

print(i)

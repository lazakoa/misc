"""
Project Euler Problem 73
========================

Consider the fraction, n/d, where n and d are positive integers. If 
n < d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending 
order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of 
reduced proper fractions for d 10,000? 
"""

"""
    I'll use the next term calculation curtesy of wikipedia.

    I know what's wrong, it's supposed to be for d = 12,000. The 
    problem got changed at some point.

"""

import fractions
import math

def next(frac1, frac2, n):
    """
        a/b, c/d, returns p/q
    """
    temp = int((n + frac1.denominator)/ frac2.denominator )
    p = (temp * frac2.numerator) - frac1.numerator
    q = (temp * frac2.denominator) - frac1.denominator
    return fractions.Fraction(p, q)


def solve(n):
    # 3332,9997 and 1,3
    start = [fractions.Fraction(3999, 11998), 
             fractions.Fraction(1,3)]
    while True:
        newval = next(start[-2], start[-1], n)
        if newval == fractions.Fraction(1,2):
            break 
        else:
            start.append(newval)
    return start



def farey_function(n):
    a, b, c, d = 0, 1, 1, n
    fracs = {fractions.Fraction(a,b), fractions.Fraction(c , d)}
    while (c <= n) or (a > 0):
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c - a), (k*d - b)
        fracs.add(fractions.Fraction(c, d))
    return len(fracs)

print(len(solve(12000)) - 2)

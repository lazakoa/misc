#/bin/env python

"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

import itertools

def sumDivisors(n):
    """
        sum of proper divisors of n
    """
    return sum(filter(lambda x: n % x == 0, range(1, (n // 2) + 1)))

def perfect(n):
    return n == sumDivisors(n)

def abundant(n):
    return sumDivisors(n) > n

def deficient(n):
    return n > sumDivisors

abun = filter(abundant, range(1, 28124))

pair = itertools.combinations_with_replacement(abun, 2)

sums = set(filter(lambda x: x < 28124, map(sum, pair)))

ints = filter(lambda x: x not in sums, range(1, 28124))

if __name__ == "__main__":
    print(sum(ints))

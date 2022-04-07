"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from general import factorize


def amicable(n):
    b = factorize(n)
    b.remove(n)
    b = sum(b)
    a = factorize(b)
    a.remove(b)
    a = sum(a)
    if a != b:
        if a == n:
            return True
        else:
            return False
    else:
        return False

print(sum([x for x in range(2,10001) if amicable(x)]))

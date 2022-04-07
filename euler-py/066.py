"""
Project Euler Problem 66
========================

Consider quadratic Diophantine equations of the form:

                              x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 =
1.

It can be assumed that there are no solutions in positive integers when D
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D 7, the largest x is
obtained when D=5.

Find the value of D 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""


"""
    * Naive method is too slow.
    * Did some reading, this is a Pell-Fermat equation. Lenstra's name shows
    up all over the place ...
    * Solving it using a continued fraction
"""

from general import contFrac, rootPeriod
from functools import reduce

squares = set(map(lambda x: x**2, range(1, 35)))
Ds = filter(lambda x: x not in squares, range(2, 1001))

def fundasol(D):
    terms = rootPeriod(D)
    k = len(terms[1:])
    if k % 2 == 0:
        ans = contFrac(terms[:-1])
    else:
        ans = contFrac(terms + terms[1:-1])
    return (ans.numerator, ans.denominator)

print(reduce(lambda x,y: x if x[1] > y[1] else y,
    map(lambda x: (x,) + fundasol(x), Ds))[0])



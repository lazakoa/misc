"""
Project Euler Problem 69
========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of numbers less than n which are relatively
prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
and relatively prime to nine, f(9)=6.

+------------------------------------------+
| n  | Relatively Prime | f(n) | n/f(n)    |
|----+------------------+------+-----------|
| 2  | 1                | 1    | 2         |
|----+------------------+------+-----------|
| 3  | 1,2              | 2    | 1.5       |
|----+------------------+------+-----------|
| 4  | 1,3              | 2    | 2         |
|----+------------------+------+-----------|
| 5  | 1,2,3,4          | 4    | 1.25      |
|----+------------------+------+-----------|
| 6  | 1,5              | 2    | 3         |
|----+------------------+------+-----------|
| 7  | 1,2,3,4,5,6      | 6    | 1.1666... |
|----+------------------+------+-----------|
| 8  | 1,3,5,7          | 4    | 2         |
|----+------------------+------+-----------|
| 9  | 1,2,4,5,7,8      | 6    | 1.5       |
|----+------------------+------+-----------|
| 10 | 1,3,7,9          | 4    | 2.5       |
+------------------------------------------+

It can be seen that n=6 produces a maximum n/f(n) for n 10.

Find the value of n 1,000,000 for which n/f(n) is a maximum.
"""

"""
    * Need Eulers totient function
    * If 
"""

from pyprimes import factorise
from fractions import Fraction
from functools import reduce

def eulerTotient(n):
    factors = list(factorise(n))
    if len(factors) == 1 and factors[0][1] == 1:
        return n - 1
    else:
        factors = list(map(lambda x: x[0], factors))
        return int(reduce(lambda x,y: x * Fraction(y - 1, y),
            factors, Fraction(n,1)))

# kinda slow, takes 1 min
print(reduce(lambda x,y: x if x[1] > y[1] else y, 
    map(lambda x: (x, x/eulerTotient(x)), range(2,1 + 10**6)))[0])



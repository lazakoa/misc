"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

from pyprimes import factorise
from collections import deque

def distinct4(n):
    return len(list(factorise(n))) == 4

def solve():
    d = deque([1,2,3,4], maxlen = 4)
    checks = deque([distinct4(i) for i in d], maxlen = 4)
    
    # This can be made MUCH MUCH faster 
    while True:
        if False not in checks:
            return d[0]
        d.append(d[-1] + 1)  
        checks.append(distinct4(d[-1]))
        
print(solve())

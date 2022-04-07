"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

from prime import prime_factorize as pf

s = set()

for i in range(1,21):
    s = s.union(set(pf(i)))

product = 1

for factor in s:
    product = product * factor

# manually add the repeated factors, 2 and 3

print(product*2*2*2*3)

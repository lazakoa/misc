"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

from prime import next_prime as np

def nth_prime(n):
    """gives the n'th prime number, 1st prime number is 2"""
    p = 2
    i = 1
    while n != i:
        p = np(p)
        i += 1
    return p

print(nth_prime(10001))

"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from prime import next_prime


def prime_list_up_to(n):
    """finds all the primes up to and including n, and returns a list"""
    plist = [2]
    while plist[-1] <= n:
        plist.append(next_prime(plist[-1]))
    if plist[-1] == n:
        return plist
    else:
        return plist[:-1]


print(sum(prime_list_up_to(2000000)))





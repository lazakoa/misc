"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

"""
    * find all 4 digit primes.
    * generate all permutations of triplets using 4 digit primes
    * sort the permutations
    * filter over all triplets s.t all elements are permutations of each other
    * make into a list and pick the tuple THAT is different from the example
"""

from pyprimes import primes_below
from itertools import combinations

p10k = set(filter(lambda x: x > 999, primes_below(9999)))

def is_perm(l):
    temp = list(map(lambda x: sorted([int(i) for i in x]),
        map(list, map(str, l))))
    return temp[0] == temp[1] and temp[1] == temp[2]

triplet = filter(is_perm, filter(lambda x: x[2] in p10k, 
        map(lambda x: (min(*x), max(*x), 2*max(*x) - min(*x)) , 
            combinations(p10k, 2))))

ans = next(triplet)

print(int(''.join(list(map(str, ans)))))


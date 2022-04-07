"""
Project Euler Problem 70
========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of positive numbers less than or equal to n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, f(9)=6.
The number 1 is considered to be relatively prime to every positive
number, so f(1)=1.

Interestingly, f(87109)=79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which f(n) is a permutation of n
and the ratio n/f(n) produces a minimum.
"""

"""
    * Find all n st f(n) = permutation of n
        * Calculate all totients for 1 < n < 10**7
    * Return the n for which n/f(n) is minimized while satisfying the 
    permutation property.
    * Can't do this naively, naive method for earlier problem took 1 minute.
    And given what i suspect about the order of growth I don't want to try 
    running this for 2 to 10**7.
"""  

"""
    * n/phi(n) is minimized when n is a prime since phi(p) = p - 1 for p a
    prime.
    * Check if there is a prime number that satisfies this what is required.
    If there is, then that is the solution.
    * If above doesn't work, then it is time to start being clever. A seive 
    of some sort would work, but would be a pain.
    * Won't work p - 1 is never a permutation of p
    * phi(n) becomes larger when n has less prime factors, and their occurence
    is kept to a minimum.
    * Use a sieve to generate all primes s.t p < 10**7 
    * Make a (p1,p2) combination using elements of that sieve
    * Filter it down & see if you get an answer
    * Since we are using pairs, we only need 10**7 // 2 primes
"""

from itertools import combinations
from pyprimes import primes_below
from functools import reduce

def is_permutation(n1, n2):
    n1 = sorted(list(str(n1)))
    n2 = sorted(list(str(n2)))
    return n1 == n2

bound = 10**7

# since the ratio is minimized when the prime factors are approxmiately of 
# the same order, we don't need to generate pair wise combinations over all 
# primes up to 10 mil.

ans = reduce(lambda x,y: x if x[0] < y[0] else y,
    map(lambda x: ((x[0]*x[1])/((x[0] - 1)*(x[1] - 1)), x),
        filter(lambda x: is_permutation(x[0]*x[1], (x[0] - 1)*(x[1] - 1)),
            filter(lambda x: (x[0] * x[1]) < bound,
                combinations(primes_below(10**5 // 2), 2)))))

print(ans[1][0] * ans[1][1])



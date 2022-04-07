"""
Project Euler Problem 50
========================

The prime 41, can be written as the sum of six consecutive primes:

                       41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a
prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

"""
    * start with a sequence length of 22
        * check all primes below 1mil for a sequence length of 22 + i
        * no convergence condition, so just check all sequences of length
        l < 100 that sum to only 1 prime
"""

from pyprimes import primes_below

p1m = list(primes_below(10**6))
p1mSet = set(p1m) # not sure if ordering is preserved & also needed for checking
maxp = p1m[-1]

# start with sequence length of 22

"""
    * create n iterators and stagger them by 1, take the topmost & use as 
    limiting condition
    * map a sum over the iterator
    * filter for prime sums
    FUCK IT, too much work
"""

def longestPrimeSum(n):
    """
    n is the length of the sequence formed by consecutive primes.
    """
    consec = []
    for i in range(len(p1m)):
        temp = sum(p1m[i:i+n])
        if temp in p1mSet: # massive speedup
            consec.append(temp)
        if temp > maxp:
            return consec
    
    return consec

def solve(n=1000):
    # set n to a bigass number initially and hope it convergers to answer
    temp = 0
    ans = []
    for i in range(22, n):
        temp = longestPrimeSum(i)
        if len(temp) != 0:
            ans = temp

    return ans[-1]

print(solve())


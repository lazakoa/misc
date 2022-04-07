"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

"""
    * definition of odd composite number: can be formed but mul of a * b
        * odd & not prime will suffice for us
    * check if a number is odd and composite,
        * keep a set of primes
            * keep a max counter and i'th index
        * keep a set of 2 * squares
            * keep a max counter and i'th index
"""

from prime import next_prime

def solve():
    primecache = {2}
    maxprime = 2
    squarecache = {2}
    squarecount = 1
    maxsquare = 2
    n = 2

    def is_oddComposite(n):
        return str(n)[-1] in ['1','3','5','7','9'] and n not in primecache

    def conj_check(n):
        temp = filter(lambda x: x in squarecache,
                (n - p for p in primecache ))
        return len(list(temp)) != 0

    while True:
        if n > maxprime:
            maxprime = next_prime(maxprime)
            primecache.add(maxprime)

        if n > maxsquare:
            squarecount += 1
            maxsquare = 2*(squarecount**2)
            squarecache.add(maxsquare)
            
        if is_oddComposite(n):
            if conj_check(n) == False:
                return n
        
        n += 1 

print(solve())

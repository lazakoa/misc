"""
Project Euler Problem 63
========================

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

"""
    * calculate the upperbound, what is the maximum that,
    * n digits ** n
    * OK, got it.
        * For each integer in n = 2, ... , 9 make an iterator that has an 
        infinite number of elements, and keep takng from the iterators until
        n**i no longer has the same number of digits as i.
    * Map over a range n = 2, ... , 9 and feed each n into a function that
    constructs the iterator specified above.
    * Map over the above range again with f s,t f returns the length of the
    iterator converted to a list. Sum over the list now.
"""

from itertools import takewhile, count

def nth(n):
    return takewhile(lambda x: len(str(n**x)) == x, count(1))

# got it! Missed 1**1 on the first try :(
print(sum(list(map(lambda x: len(list(nth(x))), range(1, 10)))))

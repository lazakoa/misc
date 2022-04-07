"""
Project Euler Problem 76
========================

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at 
least two positive integers?
"""

"""
    This can be summed up using a trick from combinatorics. Using
    the stars and bars forumla.

    Sum up for k = 2 to k = 100, using the following formula

    (n + k - 1) C (n) = (n + k - 1) C (k - 1), where k is the 
    number of containers and n is how many integers we have.
"""

"""
   Wolfram Alpha has a recurrence formula that can be written up
   later.
"""

import fractions

# made idiotic mistake, sequence starts from 0.

cache = dict()

def Partition(n):
    """
        Based on a recurrence formula listed in Wolfram, which was
        invented by Euler.
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        total = 0
        for k in range(1, n + 1):
            const = (-1)**(k+1)
            key1 = int(n - (fractions.Fraction(1/2)*k*(3*k - 1)))
            key2 = int(n - (fractions.Fraction(1/2)*k*(3*k + 1)))

            if key1 in cache:
                p1 = cache[key1]
            else:
                cache[key1] = Partition(key1)
                p1 = cache[key1]

            if key2 in cache:
                p2 = cache[key2]
            else:
                cache[key2] = Partition(key2)
                p2 = cache[key2]

            total += const*(p1 + p2)
        return total

# I didn't solve this myself. On the wiki page for Partitions, I
# found the value for p(100) where p is the partition function
#print(190569292 - 1)

print(Partition(100) - 1)





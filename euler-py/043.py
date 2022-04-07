"""
Project Euler Problem 43
========================

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1st digit, d[2] be the 2nd digit, and so on. In this
way, we note the following:

  * d[2]d[3]d[4]=406 is divisible by 2
  * d[3]d[4]d[5]=063 is divisible by 3
  * d[4]d[5]d[6]=635 is divisible by 5
  * d[5]d[6]d[7]=357 is divisible by 7
  * d[6]d[7]d[8]=572 is divisible by 11
  * d[7]d[8]d[9]=728 is divisible by 13
  * d[8]d[9]d[10]=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

"""
    * generate all the pandigital numbers from 0 to 9
        * filter out these that have 0 in first position
    * filter the pandigital numbers such that they have the above property
        * every 3 digits starting at the 2nd digit, multiply them and divide
    * sum up all the pandigital numbers
"""

from itertools import permutations
from prime import next_prime

zeroToNine = filter(lambda x: x[0] != 0, permutations(range(0,10)))

def divProp(ntup):
    """
    A function that checks for the specified property. Returns True if the
    condition is satisfied else returns false.
    """
    p = 2 
    for i in range(1, 8):
        temp = int(''.join(list(map(str, [ntup[i], ntup[i+1], ntup[i+2]]))))
        if temp % p != 0:
            return False
        p = next_prime(p)
    return True

print(sum(map(lambda x: int(''.join(map(str, x))), filter(divProp, zeroToNine))))

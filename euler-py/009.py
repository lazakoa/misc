"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
p = {frozenset((i,j)) for i in range(1,998) for j in range(1,998)}
"""

import math

def triplet(s):
    """takes a set, turns it into a list, calcultes the c value. checks if
       a + b + c = 1000, if so returns true, else false"""
    t = list(s)
    if (t[0] + t[1] + math.sqrt(t[0]**2 + t[1]**2)) == 1000:
        return True
    else:
        return False

def generate_combination(l1,l2):
    """generates all of the unique combinations for the sequences i and j"""
    temp = dict()
    for i in l1:
        for j in l2:
            if tuple(reversed((i,j))) not in temp:
                temp[(i,j)] = True
    return temp

ans = list(filter(triplet,generate_combination(range(1,998),range(1,998))))
ans = ans[0]

temp = math.sqrt(ans[0] ** 2 + ans[1] **2)

print(ans[0]*ans[1]*int(temp))



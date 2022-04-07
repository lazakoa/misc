"""
Project Euler Problem 62
========================

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
"""

def numToList(n):
    """ Takes a number and returns a sorted list. """
    return tuple(sorted(map(int,list(str(n)))))

"""
    Use the sorted digits of a cube as a key and store a list of numbers that
    contain these digits.
"""

def solve():
    d = dict()
    n = 1
    while True:
        temp = n**3
        key = numToList(temp)
        d.setdefault(key, []).append(temp)

        if len(d[key]) == 5:
            return min(d[key])
        n += 1

print(solve())



"""
Project Euler Problem 75
========================

It turns out that 12 cm is the smallest length of wire can be bent to
form a right angle triangle in exactly one way, but there are many 
more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form
a right angle triangle, and other lengths allow more than one 
solution to be found; for example, using 120 cm it is possible to 
form exactly three different right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L <=
1,500,000 can exactly one right angle triangle be formed?
"""

"""
    The L that was given here was in error. L <= 1,500,000 instead 
    of 2,000,000.

    Only consider primitive solutions. (a,b,c) in a primitive triplet
    a or b must be odd and the other even. Also gcd(a,b) = 1
"""

"""
    Pythagorean triplets using Euclid's formula. For m > n > 0,

    a = m^2 - n^2, b = m*n, c = m^2 + n^2

    Euclid's formula produces all primitive pythogorean triplets,
    but does not produce all triplets. Wolfram has a set of matrix
    transformations for generating non-primitive triplets.
"""

import math

def PythagoreanTriplets(L):
    triplets = set()
    for m in range(1, int(L**(0.5)) + 2):
        for n in range(1, int(L**(0.5)) + 2):
            if n > m:
                break
            if math.gcd(m,n) == 1:
                if (m % 2) == 0 or (n % 2) == 0:
                    a = m**2 - n**2
                    b = 2*m*n
                    triplets.add( (max(a, b), 
                                   min(a, b), 
                                   (m**2) + (n**2)))
    
    return list(filter(lambda x: sum(x) <= L, triplets))

"""
    The above function generates all primitive triplets. Take the 
    list generated and for each element keep multiplying it by 
    ever increasing numbers until the perimeter grows too big. Take
    the list that is generated from this process and create a 
    dictionary from it, where the key is perimeter and the values
    are lists of tuples representing the side lengths.
"""
def NonPrimitive(L):
    primitive = PythagoreanTriplets(L)
    nonprimitive = []
    for triplet in primitive:
        i = 2
        while True:
            temp = tuple(map(lambda x: i*x, triplet))
            if sum(temp) <= L:
                nonprimitive.append(temp)
                i += 1
            else:
                break

    return primitive + nonprimitive

def Lookup(L):
    values = NonPrimitive(L)
    ltable  = dict()

    for val in values:
        ltable.setdefault(sum(val), []).append(val)

    return ltable

def solve(L):
    table = Lookup(L)
    count = 0
    for key in table.keys():
        if len(table[key]) == 1:
            count += 1

    return count

print(solve(1500000))

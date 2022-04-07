"""
Project Euler Problem 66
========================

Consider quadratic Diophantine equations of the form:

                              x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 =
1.

It can be assumed that there are no solutions in positive integers when D
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D 7, the largest x is
obtained when D=5.

Find the value of D 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""


"""
    * For each D <= 1000, find the minimal solution.
        * Find the minimal solution?
        * Find all y s.t sqrt(1 + D*y**2) is an integer
        * First y found this way will be our minimal solution
    * Find the smallest x from the minimal solutions and give the corresponding
    D.
    
    * Naive method is too slow.
"""

from gmpy2 import iroot
from functools import reduce

def findSol(D):
    counter = 1
    while True:
        temp = 1 + D*(counter**2)
        sol = iroot(temp, 2)
        if counter % 10000000 == 0:
            print(counter)
        if sol[-1] == True:
            return (int(sol[0]), counter)
        else:
            counter += 1

squares = set(map(lambda x: x**2, range(1, 35)))

print(reduce(lambda x,y: x if x[1][0] > y[1][0] else y ,map(lambda x: (x, findSol(x)),
    filter(lambda x: x not in squares, range(2, 70))))[0])




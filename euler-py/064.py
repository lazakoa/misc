"""
Project Euler Problem 64
========================

All square roots are periodic when written as continued fractions and can
be written in the form:

N = a[0] +            1
           a[1] +         1
                  a[2] +     1
                         a[3] + ...

For example, let us consider 23:

23 = 4 + 23 -- 4 = 4 +  1  = 4 +  1     1     1 +  23 - 3
                                      23--4          7

If we continue we would get the following expansion:

23 = 4 +          1
         1 +        1
             3 +      1
                 1 +    1
                     8 + ...

The process can be summarised as follows:

a[0] = 4,     1    =   23+4    = 1 +  23--3
            23--4        7              7
a[1] = 1,     7    =  7(23+3)  = 3 +  23--3
            23--3       14              2
a[2] = 3,     2    =  2(23+3)  = 1 +  23--4
            23--3       14              7
a[3] = 1,     7    =  7(23+4)  = 8 +  23--4
            23--4        7
a[4] = 8,     1    =   23+4    = 1 +  23--3
            23--4        7              7
a[5] = 1,     7    =  7(23+3)  = 3 +  23--3
            23--3       14              2
a[6] = 3,     2    =  2(23+3)  = 1 +  23--4
            23--3       14              7
a[7] = 1,     7    =  7(23+4)  = 8 +  23--4
            23--4        7

It can be seen that the sequence is repeating. For conciseness, we use the
notation 23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
indefinitely.

The first ten continued fraction representations of (irrational) square
roots are:

2=[1;(2)], period=1
3=[1;(1,2)], period=2
5=[2;(4)], period=1
6=[2;(2,4)], period=2
7=[2;(1,1,1,4)], period=4
8=[2;(1,4)], period=2
10=[3;(6)], period=1
11=[3;(3,6)], period=2
12= [3;(2,6)], period=2
13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N 13, have an odd period.

How many continued fractions for N 10000 have an odd period?
"""

"""
    Algo for finding continued fractions
    * Given sqrt(n) start with a0 s.t a0**2 < n, check all a0's that satisfy
    the condition, algo is terminated on first one that works.
    * Start with a0 and generate 1/(sqrt(n) - a0) call this f0
    * complete the square for f0 giving us the form:
        (sqrt(n) + a0)/(n - a0**2) now we have to choose how we will factor
        out a whole number out of here, rule is as follows keep trying things
        while term sqrt(n) - a0! s.t a0!**2 < sqrt(n).
    * The algorithm is recursive, and a cache of previously seen a0's and
    fractions is kept.
"""

from itertools import takewhile, count
from copy import deepcopy
from fractions import Fraction

mastercache = set(takewhile(lambda x: x**2 < 10000, count(1)))

def rootPeriod(n):
    """ Takes an integer n s.t n > 1. Returns a list where the first element
    is a0, and the second element is a tuple indicating a repeating block in
    a continued fraction. ex [1, (2)] for n = 2
    """
    # might be faster to just rebuild this?? Doesn't matter actually
    instancecache = set(filter(lambda x: x**2 < n, mastercache))
    # block format (num, denom, +/- i) == num*(sqrt(n) +/- i)/denom
    def wrapper(a0):
        init = a0
        cond = (1, 1, -1*a0) # num, denom, a0 or a0'
        def recur(block, f): 
            f = (f[1], f[0], f[2]) # invert fraction
            if f == cond and len(block) != 0:
                return block
            else:
                # complete square
                denom = (n - (f[-1]**2))*f[1] # new denominator
                temp = Fraction(f[0], denom) # reduce fraction to lowest
                denom = temp.denominator # reduced denominator
                num = temp.numerator # reduced numerator
                # loop over all possible a0' values, a0'**2 < n
                f =  (num, denom, -1*f[2])

                branches = tee(f, n)
                if len(branches) == 0:
                    return None
                else:
                    for b in branches:
                        temp = recur(block + (b[0],),
                                (f[0], f[1], b[1]))
                        if temp != None:
                            return temp

        return recur((), cond)
    return list(filter(lambda x: x != None, map(wrapper, instancecache)))

# periods are not unique, if you allow the addition of 0 + frac then you can
# have an extended period

def tee(f, n):
    """
    returns a list of possible branches where each element in the list is
    (i, new_f[2]), where i is what will be appended and new_f is the new 
    a0' term for the fraction
    """
    temp = []
    counter = f[0] * f[2] # num * a0'
    mirror = 0
    flag = True

    if counter // f[1] != 0 and (counter % f[1])**2 < n:
        temp.append((counter // f[1], counter % f[1]))

    while flag:
        counter += f[1]
        mirror -= f[1]
        diff = (counter % f[1]) + mirror
        if diff**2 < n:
            temp.append((counter // f[1], diff))
        else:
            return temp
    return temp

# solution is ugly as shit, not happy with it :( But it did work on first try!
print(len(list(filter(lambda x: len(x[0]) % 2 != 0, filter(lambda x: len(x) != 0, map(rootPeriod, range(2, 10001)))))))


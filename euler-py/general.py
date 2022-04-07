from itertools import takewhile, count
from fractions import Fraction


def factorize(x):
    """returns a list of all the factors in a number"""
    factors = { 1: True, x:True }
    if x == 1:
        return list(factors.keys())
    else:
        counter = 2
        while counter**2 <= x:
            if counter in factors:
                counter += 1
                continue
            else:
                if x % counter == 0:
                    factors[counter] = True
                    factors[x // counter] = True
                    counter += 1
                else:
                    counter += 1
    return list(factors.keys())

def compress_spaces(s):
    """takes a string and squeezes multiple spaces into a single space"""
    if '  ' not in s:
        return s
    else:
        return compress_spaces(s.replace('  ',' '))

def rootPeriod(n):
    """ Takes an integer n s.t n > 1. Returns a list where the first element
    is a0, and the second element is a tuple indicating a repeating block in
    a continued fraction. ex [1, (2)] for n = 2
    """
    # might be faster to just rebuild this?? Doesn't matter actually
    instancecache = set(takewhile(lambda x: x**2 < n, count(1)))
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

        return (a0,) + (recur((), cond),)
    ans = list(filter(lambda x: x[1] != None, 
        map(wrapper, instancecache)))[0]

    return  (ans[0],) + ans[1]

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

    """
    if counter // f[1] != 0 and (counter % f[1])**2 < n:
        temp.append((counter // f[1], counter % f[1]))
    """
    while flag:
        counter += f[1]
        mirror -= f[1]
        diff = (counter % f[1]) + mirror
        if diff**2 < n:
            temp.append((counter // f[1], diff))
        else:
            return temp
    return temp

def contFrac(terms):
    """ Returns the rational approximation for e using the nth convergent
    fraction.
    """
    def recur(terms):
        if len(terms) == 1:
            return terms[0]
        else:
            return terms[0] + Fraction(1, recur(terms[1:]))

    return recur(terms)



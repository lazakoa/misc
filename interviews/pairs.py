#!/bin/env node

"""
    you are given a list of numbers L and a number c, return a set of
    pairs in L that adds to c if it exists else return an empty list.
"""


"""
    Assumption is that there are no repeated elements inside the list
    we are given. This assumption is made for the first function.
"""

def pairs1( L, c ):

    """
        This runs in approximately O(n). This won't pick up the 
        following: a + a = c, it doesn't use each element more than
        once. This restriction is trivial to lift.
    """

    tempSet = set(L)

    for elem in L:
        tempNum = c - elem
        ans = [elem]
        if tempNum in tempSet:
            if tempNum != elem:
                ans.append(tempNum)
        if len(ans) == 2:
            return ans

    return []

def pairs2( L, c ):
    """ 
        This one runs in O(n^2) and it doesn't have the same 
        restriction as above. It's perfectly valid to have multiple
        integers with the same value inside the list with this.
    """

    for i in range(len(L)):
        for j in range(len(L)):
            if i != j:
                a = L[i] 
                b = L[j]
                tempSum = a + b
                if tempSum == c:
                    return [a, b]
    return []

import itertools

def pairsN(N=2):
    """
        My take on the problem.
    """

    def tempf( L, c ):
        for elem in itertools.combinations( L, N ):
            if sum(elem) == c:
                return elem
        return []

    return tempf

if __name__ == "__main__":
    print(pairs1([1,2,3,4], 4))
    print(pairs2([1,2,3,4], 3))
    f = pairsN(3)
    print(f([1,2,3,4,5],7))

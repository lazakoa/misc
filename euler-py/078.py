"""
Project Euler Problem 78
========================

Let p(n) represent the number of different ways in which n coins can 
be separated into piles. For example, five coins can separated into 
piles in exactly seven different ways, so p(5)=7.

                            OOOOO

                            OOOO   O

                            OOO   OO

                            OOO   O   O

                            OO   OO   O

                            OO   O   O   O

                            O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

# this is too slow.

"""
Need a faster variant of the above, need to find a different 
recurrence.

# 05-06-2019 Finally got back to it
The following recurrence relation works:
    P(n) - P(n-1) - P(n-2) + P(n-5) + P(n-7) - P(n-12) ...

the sign of the kth term is given by (-1)**((k+1)/2) and the sum is
over generalized pentagonal numbers <= n, a pentagonal number
penta(n) = n(3n - 1)/2
"""

# why is this giving me so much trouble :(, i know the solution.
from math import floor

# correct
def pentagonal(n):

    return int((3*n*n - n) // 2)

# correct
def pentagonalList(n):
    """
    Generates all pentagonal numbers p s.t p <= n
    """

    temp = []
    i = 1

    while True:
        p1 = pentagonal(i)
        p2 = pentagonal(-i)
        
        if p1 <= n:
            temp.append(p1)
        else:
            break

        if p2 <= n:
            temp.append(p2)
        else:
            break

        i += 1

    return temp

from math import floor

def partition(n):

    partitionCache = {
            0: 1,
            1: 1,
            2: 2,
            3: 3,
            4: 5,
            5: 7,
            6: 11
            }

    pentagonalCache = pentagonalList(n)

    def p(n):
        """
        Internal function to set up recursion.
        """
        runningSum = 0
        pentagonals = list(filter(lambda x: x <= n, pentagonalCache))

        if n in partitionCache:
            return partitionCache[n]

        for i in range(len(pentagonals)):
            # i+1+1+1, due to i starting at 0 and also move to r.h.s
            k = i + 1
            sign = int((-1)**(floor((k+3)/2)))
            currentNum = n - pentagonals[i]

            if currentNum in partitionCache:
                runningSum += sign * partitionCache[currentNum]
            else:
                result = p(currentNum)
                partitionCache[currentNum] = result
                runningSum += sign * result

        return runningSum
    
    i = 5;

    while True:
        print('loop ', i)
        if p(i) % (10**6) == 0:
            print(i)
            return i

        i +=1

# least value s.t p(n) is divisible by 1 million, guessed range
#print(partition(100000))
print(55374)

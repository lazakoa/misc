#!/bin/env python

import random
import itertools
from functools import reduce

def rwalkN(d):
    """ takes the number of dimensions and returns a function that can perform
        a random walk in that space, all valid directions have equal
        probability of being chosen
    """
    
    def rwalk_nd(n):
        """ take length n and returns a function that does a 
            random walk in d dimensions
        """
        constructor = tuple(itertools.repeat(['-','+',''],d))
        mdirections = list(filter(lambda x: x.count('') == d - 1,
                                itertools.product(*constructor)))
 
        walk = (random.choice(mdirections)  for i in range(n))
        return tuple(map(lambda x: x.count('+') - x.count('-'), 
                                    reduce(helper, walk)))

    def helper(a,b): 
        """ sums two iterables, element wise and returns a iterable 
        """
        return map(lambda x: x[0] + x[1], zip(a,b))

    return rwalk_nd

if __name__ == "__main__":
    r1d = rwalkN(3)
    print(r1d(100))  #quick test

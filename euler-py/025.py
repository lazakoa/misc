#!/bin/env python

"""
Project Euler Problem 25
========================

The Fibonacci sequence is defined by the recurrence relation:

  F[n] = F[n[1]] + F[n[2]], where F[1] = 1 and F[2] = 1.

Hence the first 12 terms will be:

  F[1] = 1
  F[2] = 1
  F[3] = 2
  F[4] = 3
  F[5] = 5
  F[6] = 8
  F[7] = 13
  F[8] = 21
  F[9] = 34
  F[10] = 55
  F[11] = 89
  F[12] = 144

The 12th term, F[12], is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

import itertools

def fib(): 
    """ returns the next fibonacci number """
    a,b = 1,0
    i = 2
    while True:
        yield (a + b, i)
        a,b = a + b, a
        i += 1

ans = itertools.dropwhile(lambda x: len(str(x[0])) < 1000, fib())

if __name__ == "__main__":
    print(next(ans)[1])

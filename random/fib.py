#!/bin/env python

def fib(n):

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        f1 = 1
        f2 = 1
        total = 0

        for i in range(n - 1):
            f1, f2 = f1 + f2, f1

    return f1


def modularFibFactory(mod):
    
    def temp(n):
        
        fibSeries = []

        for i in range(n-1):
            fibSeries.append(fib(i) % mod)

        return fibSeries

    return temp

def fib7(n):
    temp = modularFibFactory(7)
    return temp(n)


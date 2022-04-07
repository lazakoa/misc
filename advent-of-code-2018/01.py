#!/bin/env python

def solve(filename):

    f = open(filename, 'r')
    freqs = []

    for line in f:
        freqs.append(int(line))

    return sum(freqs)


if __name__ == "__main__":
    print(solve('input-01.txt'))


#!/bin/env python

def readInput(filename):

    f = open(filename, 'r')
    freqs = []

    for line in f:
        freqs.append(int(line))

    return freqs


def solve(filename):

    freqs = readInput(filename)
    seen = set()
    
    running_freq = 0

    while True:
        for freq in freqs:
            running_freq += freq

            if running_freq in seen:
                return running_freq
            else:
                seen.add(running_freq)


if __name__ == "__main__":
    print(solve("input-01.txt"))


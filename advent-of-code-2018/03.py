#!/bin/env python

def readInput(filename):

    IDs = []
    f = open(filename, 'r')

    for line in f:
        IDs.append(line)

    return IDs

def segmentID(ID):

    letterCounts = dict()

    for letter in ID:
        letterCounts.setdefault(letter, 0)
        letterCounts[letter] += 1

    return letterCounts

def solve(filename):

    IDs = map(segmentID, readInput(filename))
    
    twos = 0
    threes = 0

    for ID in IDs:
        temp = ID.values()
        if 2 in temp:
            twos += 1
        if 3 in temp:
            threes += 1

    return twos * threes

if __name__ == "__main__":
    print(solve("input-02.txt"))


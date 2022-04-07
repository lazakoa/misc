#!/bin/env python

def readInput(filename):

    IDs = []
    f = open(filename, 'r')

    for line in f:
        IDs.append(line.strip())

    return IDs

def solve(filename):

    IDs = readInput(filename)
    lookupDict = dict()

    for ID in IDs:

        for i in range(len(ID)):
            tempStr = list(ID)
            tempStr[i] = "*"

            key = ''.join(tempStr)

            lookupDict.setdefault(key, [])

            lookupDict[key].append((ID, key))

    result = list(filter(lambda x: len(x) == 2, lookupDict.values()))

    return result[0][0][1].replace("*", '')

if __name__ == "__main__":
    print(solve('input-02.txt'))



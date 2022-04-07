#!/bin/env python

def loadClaims(filename):

    f = open(filename, 'r')
    claims = []

    for line in f:
        claims.append(line.strip())

    return claims

def extractID(claim):
    temp = claim.split("@")
    temp = temp[0]
    temp = temp.strip()
    temp = temp.strip("#")

    return temp

def extractOffset(claim):
    temp = claim.split("@")
    temp = temp[1]
    temp = temp.split(":")
    temp = temp[0].strip()
    a, b = temp.split(',')

    return (int(a), int(b))

def extractSize(claim):
    temp = claim.split(':')
    temp = temp[1].strip()
    a, b = temp.split('x')

    return (int(a), int(b))

def solve(filename):
    
    claims = loadClaims(filename)
    grid = dict()
    claimsDict = dict()

    for claim in claims:

        ID = extractID(claim)
        offset = extractOffset(claim)
        size = extractSize(claim)
        claimsDict[ID] = [offset, size]

        for x in range(offset[0] + 1, offset[0] + size[0] + 1):
            for y in range(offset[1] + 1, offset[1] + size[1] + 1):
                key = (x, y)
                grid.setdefault(key, [])
                grid[key].append(ID)

    squares = list(filter(lambda x: len(x) == 1, grid.values()))

    sizes = dict()

    for square in squares:
        sizes.setdefault(square[0], 0)
        sizes[square[0]] += 1

    for ID in sizes:
        temp = sizes[ID]
        size = claimsDict[ID][1]
        size = size[0] * size[1]

        if size == sizes[ID]:
            return ID

if __name__ == "__main__":
    print(solve('input-03.txt'))

#!/bin/python
"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""
from functools import reduce

f = open('resources/names.txt');
names = []

def letterToScore(ch):
    """ works, problem isn't here """
    return ord(ch) - 64


with open('resources/names.txt') as f:
    for line in f:
        names = names + list(map(lambda x: x.strip('"'), line.split(",")))


def nameToScore(name):
    """ works problem isn't here either """
    return reduce(lambda x,y: x+y, map(letterToScore, name))


# sort the names
names = sorted(names)

zipper = zip(map(nameToScore,names), range(1, len(names) + 1))
print(sum(map(lambda x: x[0] * x[1], zipper)))





"""
Project Euler Problem 74
========================

The number 145 is well known for the property that the sum of the
factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest 
chain of numbers that link back to 169; it turns out that there are 
only three such loops that exist:

169 363601 1454 169
871 45361 871
872 45362 872

It is not difficult to prove that EVERY starting number will 
eventually get stuck in a loop. For example,

69 363600 1454 169 363601 ( 1454)
78 45360 871 45361 ( 871)
540 145 ( 145)

Starting with 69 produces a chain of five non-repeating terms, but the
longest non-repeating chain with a starting number below one million 
is sixty terms.

How many chains, with a starting number below one million, contain 
exactly sixty non-repeating terms?
"""

"""
    I don't care about the contents of the chains, just need to find
    how many below a million have sixty non repeating terms.
"""

factorials = {  '0':    1,
                '1':	1,
                '2':	2,
                '3':	6,
                '4':	24,
                '5':	120,
                '6':	720,
                '7':	5040,
                '8':	40320,
                '9':	362880}

def numToSum(n):
    digits = map(lambda x: factorials[x], str(n))
    return sum(digits)

"""
    Adding the cache below cut down runtime by n > 4x. Not even the
    most effient way of doing it. Potential to store entire sequence.

    There is more that can be done, you can store every permutation
    of a number as well.
"""

cache = dict()

def chain(n):
    temp = n
    unique = set([n])
    while True:
        if temp in cache:
            temp = cache[temp]
        else:
            cache[temp] = numToSum(temp)
            temp = cache[temp]
        if temp in unique:
            return len(unique)
        unique.add(temp)

"""
print('145: ', chain(145))
print('69: ', chain(69))
print('78: ', chain(78))
print('540: ', chain(540))
"""

print(len(list(filter(lambda x: x == 60, map(chain,
    range(10**6))))))

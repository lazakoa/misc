"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def seq14a(n,d):
    s = []
    if n == 1:
        return 0 #while not strictly true assume it is 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            s.append(n)
        else:
            n = 3*n + 1
            s.append(n)
    return len(s)


def longest_seq14(n):
    """for all i < n finds all chains"""
    # i could have just computed the length of the chain here, instead of
    # the actual chains
    temp = {1: []}

    def seq14(n):
        s = [n]
        while n != 1:
            if n % 2 == 0:
                if (n // 2) in temp:
                    return s + temp[n // 2]
                else:
                    s = s + [n // 2]
                    n = n // 2
            else:
                if (3*n + 1) in temp:
                    return s + temp[3*n + 1]
                else:
                    s = s + [3*n + 1]
                    n = 3*n + 1
        return s

    for i in range(1,n):
        temp[i] = seq14(i)

    return temp

def greatest_seq14(n):
    t = longest_seq14(n)
    tnew = dict()
    for key in t:
        tnew[len(t[key])] = key
    return tnew

j = greatest_seq14(1000000)

print(j[max(j.keys())])






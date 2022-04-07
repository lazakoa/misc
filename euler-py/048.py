"""
Project Euler Problem 48
========================

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

# I know it's not meant to be solved this way!
# The proper way would break would be to do the multiply operations while 
# keeping track of 10 digits only and dropping the rest on each multiply.

def solve(n):
    temp = sum(map(lambda x: x**x, range(1, n+1)))
    
    return int(''.join(list(str(temp))[-10:]))

print(solve(1000))

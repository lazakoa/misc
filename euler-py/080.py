"""
Project Euler Problem 80
========================

It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square 
roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital 
sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the 
digital sums of the first one hundred decimal digits for all the 
irrational square
roots.
"""

"""
Algorithm for digit by digit calculation - courtesy of wikipedia.

N = (a1*(10**(n-1)) + a2*(10**(n-2)) + ... + a'n-1'*10 + an)**2

ai element of {0,1,2,...,9}

P'm-1' = Summation (i=1 to m-1, ai * 10**(n-i))
Y'm' = (2P'm-1' + am*10**(n-m))*am*10**(n-m)

Xm = X'm-1' - Ym , Xm >= 0 for all 1<=m<=n & X0 = N when Xn = 0 the
exact square root has been found if not then the sum of ai's gives a 
suitable approximation of the square root with Xn being the approx
error.
"""

def digitByDigitSqrt(x, n):
    """
    Computes the square root of x to n decimal digits.
    """

    for i in range(n+1)


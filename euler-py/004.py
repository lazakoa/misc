"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    """checks if a number is a palindrome, returns true or false"""
    if list(reversed(str(n))) == list(str(n)):
        return True
    else:
        return False

temp = range(101,1000)

print(max(filter(is_palindrome,{i*j for i in temp for j in temp})))



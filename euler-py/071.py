"""
Project Euler Problem 71
========================

Consider the fraction, n/d, where n and d are positive integers. If 
n < d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending 
order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 
3/7.

By listing the set of reduced proper fractions for d 1,000,000 in
ascending order of size, find the numerator of the fraction 
immediately to the left of 3/7.
"""

"""
    Strategy generate all fractions n/d s.t 

    Technically I only need to search through the later numbers.
"""
import fractions

def closest(d, stop):
    # yield only the closest fraction to "stop"

    for i in range(1, d + 1):
        temp = fractions.Fraction(i, d)
        if temp >= stop:
            return fractions.Fraction(i - 1, d)

def generateAnswers(d, stop):
    
    answers = set()

    for i in range(11800, d):
        answers.add(closest(i, stop))
    
    temp = list(answers)
    temp.sort()

    return temp

# this can be sped up by going backwards from the highest point, and
# simply removing elements.
print(generateAnswers(12000, fractions.Fraction(1/3))[-1])
#print(428570)

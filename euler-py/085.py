"""
Project Euler Problem 85
========================

By counting carefully it can be seen that a rectangular grid measuring 3
by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two
million rectangles, find the area of the grid with the nearest solution.

"""

def contains(h, w):
    """
    Counts the number of rectangles contained in a w*h rectangle.
    """

    return int(h*(h+1)*w*(w+1)/4)

ans = tuple()
dis = 2*10**6

for h in range(1, 2*10**6 + 1):
    for w in range(1, 2*10**6 + 1):
        temp = contains(h,w)
        tempd = abs(2*10**6 - temp)
        if tempd < dis:
            ans = (h, w)
            break


"""
Project Euler Problem 81
========================

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in red
and is equal to 2427.

                           131 673 234 103 18
                           201 96  342 965 150
                           630 803 746 422 111
                           537 699 497 121 956
                           805 732 524 37  331

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by only moving right and down.
"""

def getMatrix(filename):
    with open(filename, 'r') as f:
        matrix = []
        for line in f:
            temp = line.strip('\n')
            temp = temp.split(',')
            temp = list(map(lambda x: int(x.strip()), temp))
            matrix.append(temp)

        return matrix

"""
def solve(filename):

    matrix = getMatrix(filename)

    right = (0, 1)
    down  = (1, 0)
    moves = (right, down)
    movementCache = dict()

    def recur(matrix)

        if len(matrix) == 1 and len(matrix[0]) == 1:
"""


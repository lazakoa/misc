"""
Project Euler Problem 67
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""

from general import compress_spaces

f = open('resources/triangle.txt')
s = []
for line in f:
    s.append(line)

f.close()

s = list(map(lambda x: x.strip(),s))
s = list(map(lambda x: x.split(' '),s))
k = {i : tuple(map(int,s[i])) for i in range(len(s))}

def calc(layer):
    # layer has input format, { layer: (vertices) <- tuple}
    d = { 0: {0: (layer[0][0],layer[0])}}
    # d is like this {layer: { position: (points,(path))}}
    for i in range(1,len(layer.keys())):
        d[i] = dict()
        # loop goes down through all the layers ignoring the first
        for j in range(len(layer[i])):
            # loop goes through each layer by element
            #DEBUG print('i',i,'j',j)
            #DEBUG print(d)
            if j == 0:
                # corner case on left side, 1 valid path here
                #DEBUG print('ERROR 1')
                p1 = d[i-1][j][1] + (layer[i][j],)
                d[i][j] = (sum(p1),p1)
            elif j == (len(layer[i]) - 1):
                #DEBUG print('ERROR 2')
                # corner case on right side, 1 valid path here
                p1 = d[i-1][j-1][1] + (layer[i][j],)
                d[i][j] = (sum(p1),p1)
            else:
                #DEBUG print('ERROR 3')
                # 2 valid paths, for central elements
                #DEBUG print(j)
                p1 = d[i-1][j-1][1] + (layer[i][j],) #left
                p2 = d[i-1][j][1] + (layer[i][j],) #right
                #DEBUG print('ERROR 4')
                #DEBUG print('p1:',type(p1),p1,'p2:',type(p2),p2)
                if sum(p1) > sum(p2):
                    d[i][j] = (sum(p1),p1)
                else:
                    d[i][j] = (sum(p2),p2)

    return d

s = calc(k)

print(max([x[0] for x in s[len(s.keys())-1].values()]))



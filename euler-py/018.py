"""
Project Euler Problem 18
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                                    75
                                  95 64
                                 17 47 82
                               18 35 87 10
                              20 04 82 47 65
                            19 01 23 75 03 34
                           88 02 77 73 07 63 67
                         99 65 04 28 06 16 70 92
                        41 41 26 56 83 40 80 70 33
                      41 48 72 33 47 32 37 16 94 29
                     53 71 44 65 25 43 91 52 97 51 14
                   70 11 33 28 77 73 17 78 39 68 17 57
                  91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
               04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem
   by trying every route. However, Problem 67, is the same challenge with
a triangle containing one-hundred rows; it cannot be solved by brute
force, and requires a clever method! ;o)
"""
from general import compress_spaces

s = """\
                                    75
                                  95 64
                                 17 47 82
                               18 35 87 10
                              20 04 82 47 65
                            19 01 23 75 03 34
                           88 02 77 73 07 63 67
                         99 65 04 28 06 16 70 92
                        41 41 26 56 83 40 80 70 33
                      41 48 72 33 47 32 37 16 94 29
                     53 71 44 65 25 43 91 52 97 51 14
                   70 11 33 28 77 73 17 78 39 68 17 57
                  91 71 52 38 17 14 91 43 58 50 27 29 48
                63 66 04 68 89 53 67 30 73 16 69 87 40 31
               04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


s = list(map(lambda x: x[1:],list(map(compress_spaces,s.splitlines()))))
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










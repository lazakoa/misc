#!/bin/python

from random import randint
from random import shuffle
from random import choice

"""
   Does a random walk on a grid where each step is a letter in the alphabet. 
   The walk can terminate before the entire alphabet is exhausted. This was
   written a fairly long time ago.
"""

def image(i=10):
    """prints the completeted grid"""
    grid = setup(i)
    for i in grid:
        print(i)

def setup(size):
    grid = gen_grid(size)
    letters = gen_alpha()
    pos = [randint(1,size),randint(1,size)]
    walk(letters,grid,pos)
    return grid

def walk(letters,grid,pos):
    """the random walk"""
    #pos[0] is y axis inverted, top to bottom
    #pos[1] is x axis regular, left to right
    if move(grid,pos) == None or len(letters) == 0:
        return grid
    else:
        temp = move(grid,pos)
        tstr = grid[temp[0]]
        grid[temp[0]] = tstr[:temp[1]] + letters.pop(0) + tstr[temp[1] + 1:]
        return walk(letters,grid,temp)
        
def move(grid,pos):
    """takes the output of check and return a new position"""
    moves = list(filter(lambda x: x != None,check(grid,pos)))
    if len(moves) == 0:
        return None
    else:
        return choice(moves)

def gen_grid(i):
    """generates a grid ixi grid with 1 unit of padding"""
    s = ['!' * (i + 2)] 
    return s + [ '!' + ('#' * i) + '!' for k in range(i)] + s

def gen_alpha():
    """generates alphabet and returns the list"""
    return [chr(i) for i in range(97,123)] 

def gcf(offy,offx,grid):
    """generates a check function,takes offset on x and y and the grid"""
    def arbitrary(y,x):
        if grid[y + offy][x + offx] == '#':
            return (y + offy,x + offx)
        else:
            return None
            
    return arbitrary

def check(grid,pos):
    """checks for valid postions to go on grid"""
    #checks down, up, right, left
    return [gcf(1,0,grid)(*pos),gcf(-1,0,grid)(*pos)
            ,gcf(0,1,grid)(*pos),gcf(0,-1,grid)(*pos)]

if __name__ == "__main__":
    image()

"""
Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

"""
    * parse the text file and generate a list of words
    * map over the list of words and convert the words to numerical values
        * convert capatilized words into numerical values
    * map over the list of numbers and check if each one is a triangular number
        * check if a number is a triangular number
"""

with open('./resources/words.txt', 'r') as f:
    temp = f.read()
    temp = temp.split(',')
    wordlist = list(map(lambda x: x.strip('"'), temp))

def charToNum(char):
    """
    Converts an uppercase letter into a numerical value representing it's 
    position in the alphabet.
    """

    # A = 65
    # Z = 90
    return ord(char) - 64

def processWordList(l):

    return list(map(lambda x: sum(map(charToNum, list(x))),
        l))

cache = set(map(lambda x: (x*(x+1)) // 2, range(1, 50 + 1)))

def is_triangular(n, initialize=10):

    #cache = set(map(lambda x: (x*(x+1)) // 2, range(1, initialize + 1)))

    high = max(cache)

    if n <= high:
        if n in cache:
            return True
        else:
            return False
    else:
        print('too lazy to write it')
        # compute the value and add it to cache
        pass

print(len(list(filter(is_triangular, processWordList(wordlist)))))







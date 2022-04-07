"""
Project Euler Problem 79
========================

A common security method used for online banking is to ask the user 
for three random characters from a passcode. For example, if the 
passcode was 531278, they may asked for the 2nd, 3rd, and 5th 
characters; the expected reply would be: 317.

The text file keylog.txt contains fifty successful login attempts.

Given that the three characters are always asked for in order, 
analyse the file so as to determine the shortest possible secret 
passcode of unknown length.
"""

f = open('resources/keylog.txt', 'r')

sequences = []

for line in f:
    i1, i2 , i3 , nl = line
    sequences.append((i1, i2, i3))

def reverseVerify(sequence, passcode):

    counter = 0;
    temp = passcode #map(int, list(str(passcode)))

    for number in temp:
        if number == sequence[counter]:
            counter += 1
            if counter == 3:
                return True

    return False

def verifyFactory(sequence):

    def temp(passcode):
        return reverseVerify(sequence, passcode)

    return temp

funcList = list(map(verifyFactory, sequences))

"""
Brute force failed, second approach is to look at what digits appear
inside the keylog file and construct all possible numbers from the set
of valid digits.
"""

def validDigits(sequences):

    result = set()

    for sequence in sequences:
        for number in sequence:
            result.add(number)

    return result

from itertools import product

"""
for perm in product(validDigits(sequences), repeat=8):

    tally = []

    for func in funcList:

        if func(perm) == True:
            tally.append(True)

        if len(tally) == 50:
            print(perm)
"""

# Ran above code to find the following:
# 73162893 doesn't work, cause i'm a idiot and used ints instead of str
print("73162890")


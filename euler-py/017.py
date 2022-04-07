"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

def convert(n):
    """takes a int and returns the interger written in words"""
    s = { 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
         60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
        100: 'one hundred', 1000: 'one thousand', 0: ''}

    n1 = str(n).zfill(4)
    n = (n1[0],n1[1],n1[-2:])

    def onek(n1,n):
        if int(n[0]) == 1:
            return s[1000]
        else:
            return ''

    def hunds(n1,n):
        if int(n[1]) > 0:
            return s[int(n[1])] + ' hundred'
        else:
            return ''

    def teens(n1,n):
        k = ''
        if int(n[1]) != 0 and int(n[2]) != 0:
            k = ' and '
        else:
            pass

        if int(n[2]) < 20:
            k = k + s[int(n[2])]
        elif int(n[2]) % 10 == 0:
            k = k + s[int(n[2])]
        else:
            k = k + s[int(int(n[2][0])*10)] + '-' + s[int(n[2][1])]
        return k
    return onek(n1,n) + hunds(n1,n) + teens(n1,n)

def conv_wrap(x):
    t = convert(x).replace(' ','')
    return t.replace('-','')

s = list(map(conv_wrap,range(1,1001)))

print(sum(map(len,s)))

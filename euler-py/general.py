
def factorize(x):
    """returns a list of all the factors in a number"""
    factors = { 1: True, x:True }
    if x == 1:
        return list(factors.keys())
    else:
        counter = 2
        while counter**2 <= x:
            if counter in factors:
                counter += 1
                continue
            else:
                if x % counter == 0:
                    factors[counter] = True
                    factors[x // counter] = True
                    counter += 1
                else:
                    counter += 1
    return list(factors.keys())

def compress_spaces(s):
    """takes a string and squeezes multiple spaces into a single space"""
    if '  ' not in s:
        return s
    else:
        return compress_spaces(s.replace('  ',' '))


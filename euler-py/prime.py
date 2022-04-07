"""
    module for working with prime numbers

"""

"""
    still needs primality tests and a seive
"""

def prime_factorize(n):
    """does a prime factorization, factors can show up multiple times"""
    s = 2
    factors = []
    while not is_prime(n):
        if n % s == 0:
            n = n // s
            factors.append(s)
        else:
            s = next_prime(s)

    factors.append(n)
    return factors

def unique_prime_factors(n):
    """returns all the unique prime factors of n"""
    return set(prime_factorize(n))

def is_prime(n):
    """checks if a number is prime, works on 2 too"""
    x = 2
    while x*x <= n:
        if x*x == n:
            return False
        elif n % x == 0:
            return False
        else:
            x = x + 1
    return True

def next_prime(p):
    """takes a prime number and spits out the next prime number"""
    i = p + 1
    if is_prime(p) == False:
        print('function only accepts prime numbers')
        return None
    else:
        while is_prime(i) == False:
            i = i + 1
    return i

def nth_prime(n):
    """gives the n'th prime number, 1st prime number is 2"""
    p = 2
    i = 1
    while n != i:
        p = next_prime(p)
        i += 1
    return p

def prime_list_up_to(n):
    """finds all the primes up to and including n, and returns a list"""
    plist = [2]
    while plist[-1] <= n:
        plist.append(next_prime(plist[-1]))
    if plist[-1] == n:
        return plist
    else:
        return plist[:-1]

        

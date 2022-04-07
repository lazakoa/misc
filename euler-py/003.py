"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

### factor out all the primes continously
def prime_factorize(n):
    """does a prime factorization, only gives factors not their frequency"""
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

if __name__ == '__main__':
    print(max(prime_factorize(600851475143)))

        
        

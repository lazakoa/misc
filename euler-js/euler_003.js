/*
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
*/

function primeFactorize(x) {
    var current = 2;
    var factors = [];
    while (!(checkPrime(x))) {
        if (x % current === 0) {
            x = x / current;
            factors.push(current);
        }
        else {
            current = nextPrime(current);
        }
    }
    if (factors.includes(x)) {
        return factors;
    }
    else {
        factors.push(x);
        return factors;
    }
}



function nextPrime(x) {
    // Takes a number and returns the next prime number after it.
    x += 1;
    while (checkPrime(x) == false) {
        x += 1;
    }
    return x;
}

function checkPrime(x) {
    if (x === 1) {
        return false;
    }
    else {
        for (var counter = 2; counter * counter <= x; counter++) {
            if ( x % counter === 0) 
                return false;
        }
    }
    return true;
}

console.log(primeFactorize(600851475143).reduce(function(a, b) {
    if (a > b) {
        return a;
    }
    else {
        return b;
    }
}));


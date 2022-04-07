/*
Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

var lo = require('lodash');

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

function nextPrime(x) {
    // Takes a number and returns the next prime number after it.
    x += 1;
    while (checkPrime(x) == false) {
        x += 1;
    }
    return x;
}

function genPrimes(x) {
    // generate all primes less than x or equal to x.
    var primes = [2];
    while (primes[primes.length - 1]  <  x) {
        var temp = primes[primes.length - 1];
        primes.push(nextPrime(temp));
    }
    primes.pop();
    return primes;
}

console.log(lo.sum(genPrimes(2*(10**6))));

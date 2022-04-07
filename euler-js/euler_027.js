/*
Problem 27: Quadratic primes

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
*/

/* This looks like a great excuse to try out generators in js */

var lo = require('lodash');

// reusing this function from problem 11, nvm blows the stack in this case
function combinations(array, n) {
    // Returns every possible n,n-1,n-2,. ..-tuple that can be constructed 
    // from elements in array, This is so ugly I want to cry & all because js 
    // has no immutable tuples. I could do this with raw objects I think? 
    
    var temp = new Set();

    function recur(s, array, dimensions ) {
        if (dimensions === 0) {
            return s;
        }
        else {
            for (var elem in array) {
                var value = recur(s + ',' + String(array[elem]), 
                                array, dimensions - 1);
                temp.add(value);
            }
        }
        return s;
    }
    recur('', array, n);
    
    var output = [];
    for (let e of temp) {
        output.push(e.slice(1).split(',').map(Number));
    }
    // ugliness ends here
    
    return output;
}

function permutations(array, n) {
    return lo.filter(combinations(array, n), (x) => { return x.length ===  n });
}

function checkPrime(x) {

    if (x < 1) {
        return false;
    }

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

function makeFormula(a, b) {
    function temp(n) {
        // I need to preserve the internal state here
        return n*n + (a * n) + b;
    }
    return temp;
}

function* genFromFormula(f, check) {
    // takes function f that does some sort of computation, and makes an 
    // generator that computes successive terms f(n) for n = 0 ... k where k
    // is the last integer for which check(f(k)) fails.
    var n = 0;
    var temp = f(n);

    while (check(temp)) {
        yield temp;
        n++;
        temp = f(n);
    }
    // this tosses out a undefined when it ends

}

function drain(iterator) {
    // drains an iterator
    var counter = 0;
    for (let value of iterator) {
        counter++;
    }
    return counter;
}

/* 
// quick test used to check for off by one errors in drain.
function* ranger(n) {
    var counter = 0;
    while (counter < n) {
        yield counter++;
    }
}
*/

// Slow and memory hungry, there are a few cheap ways to shave down the runtime
// will do it only if necessary. An array of 4 million functions is around
// 600mb ~ 800mb of memory. 
// I know that I only need to check formulas for b === prime.

var temp = lo.map(permutations(lo.range(-999,1000), 2), 
    (x) => { return { a: x[0], 
                      b: x[1],
                      total: drain(genFromFormula(makeFormula(x[0], x[1]),
                                           checkPrime))};});


// forEach would have been better here I think, performance difference?
// actually it didn't matter, nearly 4 mil values were gone over before I 
// even noticed anything happening.

// this gets mutated 
//  |
//  v

var max = {total: 0};


var temp = lo.map(temp, (x) => { if ( x.total >= max.total) {
                                        max = x;
                                    } return x;}) 

// a = -61 & b = 971, takes about 5 seconds I think.

console.log(max.a * max.b);



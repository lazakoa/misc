/*
Problem 34: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
*/

// 9 digits generate a sum of 7 digits
// 7 digits generate a sum of 7 digits. Use this as the upper bound.
// 9! = 362880 (maximum a single digit can generate)
// 8! = 40320

var wu = require('wu');

function factorial(n) {
    if (n === 0) {
        return 1;
    }
    var total = 1;
    for (var counter = 0; counter < n;) {
        counter++;
        total = total * counter;
    }
    return total;
}

function genCache(n) {
    var cache = {};
    for (var counter = 0; counter < n + 1; counter++) {
        cache[counter] = factorial(counter);
    }
    return cache;
}

factorialCache = genCache(9);

function isValid(x) {
    var temp = String(x).split('');
    total = 0;
    for (var digit of temp) {
            total += factorialCache[digit];
    }
    return x === total;
}

function* rangeIter(start, end) {
    for (var counter = start; counter < end; counter ++) {
        yield counter;
    }
}    

var f1 = wu(rangeIter(3, (factorialCache[9] * 7) + 1)).filter(isValid);

console.log(wu(f1).reduce((a, b) => a + b));


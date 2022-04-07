#!/bin/env node
/*
Problem 57: Square root convergents

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

            2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in
the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
*/

/* This would be so easy in python but w/e
 * 1. Find a fraction library for js
 * 2. This can be done in a nice way using recursion + a cache.
 * 3. Find the expansion for every n s.t 8 <= n <= 1000
 */

var bigInt = require("big-integer");

function solve(n) {
    /* 1/1, 3/2, 7,5, 17,12, 41,29
     *
     */
    var num = bigInt(1);
    var den = bigInt(1);
    var temp = den;
    var counter = 0;
    for (var i = 0; i < n; i++) {
        temp = den;
        den = num.add(den);
        num = den.add(temp);
        if (aMoreDigitsB(num, den)) {
            counter++;
        }
    }
    return counter;
}

function aMoreDigitsB(a, b) {
    var n1 = String(a);
    var n2 = String(b);
    if (n1.length > n2.length) {
        return true;
    } else {
        return false;
    }
}

console.log(solve(1000));

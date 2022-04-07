#!/bin/env node
/*
Problem 51: Prime digit replacements

By replacing the 1st digit of *57, it turns out that six of the possible
values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with
this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
*/

/* Naive attemp too slow also incorrect somewhere.
*/

var lo = require('lodash');
var wu = require('wu');
var G = require('generatorics');
var pri = require('primality');

/* Generate all primes that have n digits. Use this as our cache.
 * For every 5 digit number --> slice out digits randomly.
 */

// sieve is too fucking slow, just do pri.primality
function nDigitPrimes(n) {
    return lo.filter(lo.range(10**(n-1), (10**(n)) - 1),
        pri.primality);
}

//var cache = lo.filter(lo.range(10**8), pri.primality);

/* Make a generator that returns digit positions.
 * swap 1, swap 2, swap 3, ect, until swap n - 1
 * Given a digit position stick all possible numbers in it 0 to 9. At least 
 * 8 of these should be prime.
 */

// wanted to use a generator for this :( But below is much simpler

function generatePositions(n) {
    var temp = [];
    for (var i = 1; i < n ; i++) {
        for (var pos of positions(n, i)) {
            temp.push(pos.slice()); // prevents mutation 
        }
    }
    return temp;
}

function positions(n, i) {
    return G.combination(lo.range(0, n), i);
}

function generateFamily(number, position) {
    var family = []; 
    for (var n of lo.range(0, 10)) {
        var temp = String(number).split('');
        for (var pos of position) {
                temp[pos] = String(n);
        }
        // 0 at the front truncates the number, do we want this?
        temp = Number(temp.join(''));
        if (String(temp).length === String(number).length) {
            family.push(temp);
        }
    }
    return family;
}


// For each prime, calculate all the possible positions, and for each possible
// position calculate all the possible digit entries.
// Primes * (combinations made up of 0,...,n-1 from 1 to n-1 items) * 10
// For n = 5 there are 8363 primes * 30 * 10 * primality check(constant)
// For n = 6 there are 68906 primes * 62 * 10
// For n = 7 there are 586081 primes * 126 * 10

function solve(n) {
    // n is the number of primes in the family
    var cache = new Set(nDigitPrimes(1)); // cache
    for (var i = 2;; i++) {
        var digits = nDigitPrimes(i);
        cache = new Set(digits);
        var positions = generatePositions(i);
        for (digit of digits) {
            for (var position of positions) {
                var temp = generateFamily(digit, position);
                if (lo.filter(temp, x => cache.has(x)).length === n) {
                    return temp;
                }
            }
        }
    }
}

// why the fuck is this not a default method?
Set.prototype.union = function(setB) {
    var union = new Set(this);
    for (var elem of setB) {
        union.add(elem);
    }
    return union;
}

// works
console.log(lo.min(lo.filter(solve(8), pri.primality)));

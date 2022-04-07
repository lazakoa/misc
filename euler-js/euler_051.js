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

/* 
    * Generate a cache of primes (below 1 million)
    * Loop over all of the primes in the cache
        * Do a swap of pairs of digits in the number with 00 to 99
            * need to generate positions in the number using a combination
    * If cache is exhausted, generate a cache of primes below 10 million and
    repeat. Answer is first prime to satisfy the property of having a eight
    prime value family.
*/

var lo = require('lodash');
var wu = require('wu');
var G = require('generatorics');
var pri = require('primality');

/* Generate all primes that have n digits. Use this as our cache.
 */

// sieve is too fucking slow, just do pri.primality
function nDigitPrimes(n) {
    return lo.filter(lo.range(10**(n-1), (10**(n)) - 1),
        pri.primality);
}

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

function generateFamily(number, positions) {
    var family = []; 
    for (var n of lo.range(0, 10)) {
        var temp = String(number).split('');
        for (var position of positions) {
                temp[position] = String(n);
        }
        family.push(Number(temp.join('')));
    }
    return family;
}

function solve(n) {
    // n is the number of primes in the family
    var primes = new Set();
    for (var i = 2;; i++) {
        var ndigit = nDigitPrimes(i);
        primes = primes.union(new Set(nDigitPrimes(i)));
        var positions = generatePositions(i);
        console.log(i);
        for (var prime of ndigit) {
            for (var pos of positions) {
            var family = generateFamily(prime, pos);
            }
            var temp = lo.filter(family, (x) => primes.has(x));
            if (temp.length === n) {
                return lo.min(temp);
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

console.log(solve(6));

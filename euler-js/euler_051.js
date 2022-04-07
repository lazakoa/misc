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
var nu = require('numbers');
var G = require('generatorics');

comb = [];
for (var comb of G.combination(lo.range(6), 2)) {
  console.log(comb);
}

function digitSwap(p) {
    /* Takes a integer p, computes all the possible positions where digits
     * can be replaces, and creates all the possible numbers that can be 
     * formed by pushing 0 and 9 to these positions.
     */
    length = lo.range(String(p).length);
    positions = G.combination(length, 2);

}

function pairSwap(l) {

}



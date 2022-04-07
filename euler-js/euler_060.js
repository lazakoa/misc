#!/bin/env node
/*
Problem 60: Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
*/

/* The property that you need to satisfy is that given 5 primes, take any two
 * and concatenate them in any order the resulting number is still al prime.
 *
 * Find the lowest sum for a set of five primes that satisfy this propery.
 * 
 * If any of 5 concatenate into primes, then any of four concatenate into 
 * primes. 792 is the lowest sum works for 4. Check all primes > 673 until
 * condition is satisfied.
 */

/* No way you can check all the combinations.
 * 1. Use [3, 7, 109, 673] as a base solution.
 * 2. Try to find a prime p s.t p > 673 for which the property is satisifed
 * for every element in the base solution.
 *
 * Lets call the number we are looking for n.
 * 3-n and n-3 both are prime
 * 7-n and n-7 both are prime
 * 109-n and n-109 both are prime
 * 673-n and n-673 both are prime
 */

var pri = require('primality');
var lo = require('lodash');

function concat(p1, p2) {
    var t1 = String(p1) + String(p2);
    var t2 = String(p2) + String(p1);
    return pri.primality(Number(t1)) && pri.primality(Number(t2));
}

var base = [20887, 7, 109, 673];

function check(i) {
    for (var b of base) {
        if (!(concat(b,i))) {
            return false;
        }
    }
    return true;
}

var primes = new Set();

function solve() {
    var start = 4;
    for (var i = start;; i++) {
        if (pri.primality(i)) {
            if (check(i)) {
                return i;
            }
        }
    }
}

console.log(solve());


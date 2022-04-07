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

/* No way you can check all the combinations.
 *
 * Define concat(a,b) to be a function that returns a tuple s.t the first
 * element of the tuple is the digits of b appened to the end of the digits
 * of a, and vice versa for the second element of the tuple.
 *
 * concat(a,b) is equivalent to a*(10**(digits(b))) + b and 
 * b*(10**(digits(a))) + a.
 *
 * Definition of remarkable:
 * A set of primes called P is said to be remarkable if for every pi,pj s.t
 * pi != pj and where every element in the tuple concat(pi,pj) is prime. If 
 * there are n primes in the set P then there are combination(n,2) possible 
 * pairs pi, pj s.t pi != pj.
 *
 * Take pi, pj from the set P s.t pi != pj. If concat(pi,pj) then 
 * digits(concat(pi,pj)) = digits(pi) + digits(pj).
 *
 * Assume that the set P is drawn from a set P' s.t P' consists of all primes
 * p < b for some positive natural number b. combination(Ord(P'), Ord(P)) 
 * gives an upper bound on the total number of sets P that are possible.
 *
 * There are 168 primes s.t p < 1000.
 * There are 1229 primes s.t p < 10000.
 *
 * The sum of five primes that satisfy this property is less than or equal
 * to ~70million.
 *
 * 1. Can't be solved by brute force easily (possible, not recommended)
 * 2. Doing a tree search to generate all possible 5 prime solutions is not
 * feasible even for a low number of primes to search over. Also it is not 
 * known when convergence will occur.
 *
 * Idea:
 * Let the set P be all primes less than or equal to some n. Where n is chosen
 * arbitrarily. Generate all pairs pi,pj E P s.t pi != pj. Filter out all the
 * pairs pi,pj that are not remarkable. *Somehow* chain together k pairs s.t
 * (pi1,pj1) --> .... -> (pik,pjk) is remarkable when only the unique pi's and
 * pj's are considered.
 *
 */

var pri = require('primality');
var lo = require('lodash');

function concat(p1, p2) {
    var t1 = String(p1) + String(p2);
    var t2 = String(p2) + String(p1);
    if (Number(t1) in primes && Number(t2) in primes) {
        return true;
    } else if (Number(t1) in primes) {
        var b2 = pri.primality(Number(t2));
        if (b2) {
            primes.add(Number(t2))
            return true ;
        } else {
            return false;
        }
    } else if (Number(t2) in primes) {
        var b1 = pri.primality(Number(t1));
        if (b1) {
            primes.add(Number(t1));
        }
    } else {
        var b1 = pri.primality(Number(t1));
        var b2 = pri.primality(Number(t2));
        if (b1) {
            primes.add(Number(t1));
        }
        if (b2) {
            primes.add(Number(t2))
        }
        return pri.primality(Number(t1)) && pri.primality(Number(t2));
    }
}

//var base = [11, 113, 1217, 75659, 70816763]; // 70 million
//var base = [3, 7, 109, 673, 129976621]; // 130 million


function check(i) {
    for (var b of base) {
        if (!(concat(b,i))) {
            return false;
        }
    }
    return true;
}

var primes = new Set(lo.filter(lo.range(10**8), pri.primality));

function solve() {
    var start = 24;
    console.time(2);
    for (var i = start;; i++) {
        if (0 === i % 10**8) {
            console.timeEnd(2);
        }
        if (i in primes) { 
            if (check(i)) {
                return i;
            }
        } else if (pri.primality(i)) {
            if (check(i)) {
                return i;
            }
        }
    }
}

//console.log(lo.sum(base));
console.log(solve());


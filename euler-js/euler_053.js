#!/bin/env node
/*
Problem 53: Combinatoric selections

There are exactly ten ways of selecting three from five, 12345:

           123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, nCr(5,3) = 10.

In general,

nCr(n,r) = n!/(r!(n-r)!), where r =< n, n! = n * (n1) * ... * 3 * 2 * 1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: nCr(23,10) =
1144066.

How many values of nCr(n,r), for 1 =< n =< 100, are greater than one-million?
*/

/* For each n s.t  1 <= n <= 100 & r s.t r <= n find all nCr(n,r) s.t 
 * nCr(n,r) > 10**6.
 *
 * Naive implementation of nCr(n,r) is slow and will probably overflow js int
 * into Infinity. Test? Doesn't flow into Infinity but doesn't matter will
 * try different approach.
 *
 * Useful definitions (courtesy of wikipedia)
 *
 * 1. nCr(n, k+1) = (n-k)*nCr(n,k) / (k + 1)
 * 2. nCr(n,k) = nCr(n-1, k-1) + nCr(n-1, k)
 *
 * If nCr(n-1, k) > 10**6 then nCr(n,k) > 10**6. The first value n for which
 * nCr(n,k) is greater than 10**6 is 23, ie nCr(23,10). Hence for all i s.t
 * 23 < i <= 100, nCr(i, 10) > 10**6.
 *
 * For each i s.t 23 < i <= 100. Take nCr(i, k) with k s.t 1 <= k < 10 and 
 * apply propery 1 in a backwards fashion to bind the lower bound for k 
 * s.t  nCr(i, k) < 10**6.
 *
 * Don't need to do the above, since the ratio below only decreases.
 *
 * (k + 1) * nCr(n, k+1) / (n - k) = nCr(n,k)
 *
 * Actually wait I do need it. Find the lower bound and symmetrically apply it
 * as 100 - lowerbound to get the upper bound. The values of k for which you 
 * have an answer is everything in between the two bounds.
 * 
 * First value of n that works is 
 *
 * nCr(24, 9) ~ 1.3mil and nCr(24, 15) is the same.
 * nCr(25, 8) ~ 1mil and nCr(25, 17) is the same.
 * nCr(26, 8) ~ 1.5mil and nCr(26, 18) is the same.
 * ...
 * nCr(30, 7) ~ 2mil
 * nCr(100,4) ~ 3.9mil and nCr(100,96) is the same.
 *
 * 
 */

var lo = require('lodash');

function nCr(n,k) {
    // shamelessly copied from wikipedia
    if (k < 0 || k > n) {
        return 0;
    }
    if (k === 0 || k === n) {
        return 1;
    }
    k = Math.min(k, n - k);
    coeff = 1;
    for (var counter = 0; counter < k; counter++) {
        coeff = (coeff * (n - counter)) / (counter + 1);
    }
    return coeff;
}

function nCrBound(n, bound) {
    coeff = 1;
    for (var counter = 0;; counter++) {
        coeff = (coeff * (n - counter)) / (counter + 1);
        if (coeff >= bound) {
            return counter + 1;
        }
    }
    return 0;
}

console.log(lo.sum(lo.map(lo.range(23, 101), (x) => {
                var temp = nCrBound(x, 10**6);
                    return (x - temp) - temp + 1;})));



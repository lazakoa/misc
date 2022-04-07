#!/bin/env node
/*
Problem 52: Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
*/

/*
 * Need to only check numbers that have a leading 1.
 *
 * So 10-19, 100-199, 1000-1999, and etc. Can be trimmed down even further.
 * Only take 70% of the interval and use:
 *
 * 10-17, 100-170, 1000-17000, and etc.
 *
 */

function solve() {

    for (var pow = 1;; pow++) {
        for (var b = 10**pow; b < (10**pow + 7*(10**(pow - 1))); b++){
            if (check6x(b)) {
                return b;
            }
        }
    }
}

check6x = checkMultiples(6);

function checkMultiples(n) {

    function f(x) {
        temp = digitsFromInt(x);
        for (var counter = 2; counter < (n + 1) ; counter++) {
            if (temp !== digitsFromInt(x * counter)) {
                return false;
            }
        }
        return true;
    }
    return f;
}

function digitsFromInt(n) {
    return String(n).split('').sort().join('');
}

console.log(solve());


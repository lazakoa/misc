/*
Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

/*
 * a + b + Sqrt(a^2 + b^2) = 1000
 */

var lo = require('lodash');

function pythTriplet(x) {
    for (var i = 1; i < 501; i++) {
        for (var j = 1; j < 501; j++) {
            var temp = Math.sqrt(i**2 + j**2);
            if (isSquare(temp)) {
                if (i + j + temp === 1000) {
                    return [i, j, 1000 - i - j];
                }
            }
        }
    }
}

function isSquare(x) {
    return Math.floor(x) === Math.ceil(x);
}

console.log(lo.reduce(pythTriplet(1000), function(a, b) {
    return a * b; }));



/*
Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
*/

var lo = require('lodash');

var a = lo.sum(lo.map(lo.range(1, 101), function(x) { return x*x;}));

var b = lo.sum(lo.range(1, 101)) ** 2

console.log(b - a);

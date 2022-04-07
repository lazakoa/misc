/*
Problem 30: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

  1634 = 1^4 + 6^4 + 3^4 + 4^4
  8208 = 8^4 + 2^4 + 0^4 + 8^4
  9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
*/

// 999999 with each digits ^5 is 354294, use that as the upperbound

var lo = require('lodash');

function raiseDigits(x, n) {
    // raises the digits of x to the n'th power and returns the sum
    return lo.reduce(lo.map(String(x).split(''), (x) => {
        return Number(x)**n;}), (a, b) => {
            return a + b;});
}
    
console.log(lo.reduce(lo.filter(lo.range(2, 354294), (x) => { 
    return x === raiseDigits(x, 5);}), (a, b) => { return a + b;}));







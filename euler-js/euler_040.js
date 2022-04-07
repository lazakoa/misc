/*
Problem 40: Champernowne's constant

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
*/

// d[1] = 1
// d[10] = 1

var lo = require('lodash');

function champernowne(n) {
    // n specifies the maximum number of digits, returns first occurence of
    // when it goes over
    var constant = '';
    for (var i = 1; constant.length <= n; i++) {
        constant = constant + String(i);
    }
    return constant;
}

function solve(n) {
    var indices = lo.range(n + 1).map( x => 10**x );
    var sum = 1;
    const c = champernowne(indices[indices.length - 1]);
    for (var indice of indices) {
        sum *= Number(c[indice - 1]);
    }
    return sum;
}

console.log(solve(6));
     

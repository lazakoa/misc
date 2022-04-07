/*
Problem 32: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
*/

// find all pairs a b st in  [a, b, a*b] all the digits 1 to 9 show up exactly
// once

var lo = require('lodash');
var G = require('generatorics'); // <-- omg so happy
var wu = require('wu');

function isPandigital(x) {
    if (x.length !== 9) {
        return false;
    }
    var temp2 = new Set(x.split(''));
    
    if (temp2.has('0')) {
        return false;
    }
    else {
        if (temp2.size === 9) {
            return true;
        }
        else {
            return false;
        }
    }
}

// messing around with wu + iterators, it's pretty fast now.

var range = lo.filter(lo.range(1, 5000), (x) => {
                var temp1 = String(x).split('');
                var temp2 = new Set(temp1);
                return temp1.length === temp2.size; })

var temp = wu(G.combination(range, 2)).filter( (i) => {
    return isPandigital(String(i[0]) + String(i[1]) + String(i[0] * i[1]));});

var cache = new Set();

var total = wu(wu.map((x) => {
            var product = x[0] * x[1];
            if (cache.has(product)) {
                return 0;
            }
            else {
                cache.add(product);
                return product;
            }
        } , temp)).reduce((a, b) => a + b);

console.log(total);





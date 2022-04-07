/*
Problem 35: Circular primes

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
*/

var lo = require('lodash');
var prime = require('./prime');
var G = require('generatorics');

function isCircularPrime(x) {
    var temp = String(x).split('')
    var tail;
    var head;
    for (var counter = 0; counter < temp.length; counter++) {
        if (!prime.checkPrime(Number(temp.join('')))) {
            return false;
        }
        tail = temp.pop();
        temp.unshift(tail);
    }
    return true;
}

console.log(lo.filter(lo.range(2, 1 + 10**6), isCircularPrime).length);

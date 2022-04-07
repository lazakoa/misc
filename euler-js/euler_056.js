#!/bin/env node
/*
Problem 56: Powerful digit sum

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is
the maximum digital sum?
*/

/* 
 * 1. Make a generator that yields all permutations of [0,99]
 * 2. Map over the generator and use big int to perform a^b
 * 3. Map over the generator of bigInts and create the digital sum
 * 4. Reduce over the digital sums to find the maximum digital sum
 */

var lo = require('lodash');
var wu = require('wu');
var bigInt = require('big-integer');
var G = require('generatorics');


function digitalSum(n) {
    return lo.sum(lo.map(String(n).split(''), Number));
}

function helper(array) {
    return lo.sum(lo.map(array, digitalSum));
}

k = wu(G.permutation(lo.range(0,100), 2)).map( (x) => {
    return bigInt(x[0]).pow(x[1]);}).map( (x) => { 
        return helper(x.value);}).reduce( (x, y) => {
            if (x > y) {
                return x;
            } else {
                return y;
            }});

console.log(k);

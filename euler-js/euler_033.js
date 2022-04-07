/*
Problem 33: Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
*/

// 2 digits in numerator & denominator, less than 1 in value, 4 total

/* 
 * generate 2 digit numerator denominator pairs
 * filter out all fractions with value greater than 1
 *
 * for each pair/fraction left generate the 4 possible permutations below
 * [ tf, tf] [ tf, ft] [ ft, ft] [ ft, tf] see if any of them are the same as
 * the original fraction
 *
 */

var G = require('generatorics');
var lo = require('lodash');
var wu = require('wu');
var prime = require('./prime.js');

function numberToDigits(x) {
    return lo.map(String(x).split(''), Number);
}

function isDigitCancellingFraction(array) {
    // array[0] is numerator & array[1] is denominator
    var num = String(array[0]).split('');
    var den = String(array[1]).split('');
    var cnum = pruneBy(num, den).join('');
    var cden = pruneBy(den, num).join('');
    
    if (cnum === '') {
        return false;
    }
    if (num.length === cnum.length) {
        return false;
    }

    if ((Number(cnum) / Number(cden)) === (array[0] / array[1])) {
        return true;
    } else {
        return false;
    }
}

function pruneBy(array1, array2) {
    // removes elements in array1 that are in array2
    var temp = [];
    var copy2 = array2.slice();

    for (var elem of array1) {
        if (copy2.indexOf(elem) === -1) {
            temp.push(elem);
        } 
        else {
            var i = copy2.indexOf(elem);
            copy2 = copy2.slice(0,i).concat(copy2.splice(i + 1));
        }
    }
    return temp;
}

function lowestTerms(fraction) {
    // fraction === [numerator, denominator];
    var fnum = prime.decompose(fraction[0]);
    var fden = prime.decompose(fraction[1]);
    return [lo.reduce(pruneBy(fnum, fden).concat([1]), (a, b) => a * b),
            lo.reduce(pruneBy(fden, fnum).concat([1]), (a, b) => a * b)];
}

function isLowestTerms(fraction) {
    var temp = lowestTerms(fraction)
    return false;
}

// filter out everything greater than 1
var f1 =  wu(G.permutation(lo.range(10,100), 2)).filter( (x) => {
    return (x[0] / x[1]) < 1;});

// 26/65
// 16/64
// 19/95
// 49/98

// leave only digit cancelling fractions

var f2 = wu(f1).filter(isDigitCancellingFraction);

var f3 = wu(f2).filter( x => {
    return !((x[0] % 10 === 0) && (x[1] % 10 === 0));});

console.log(lowestTerms(wu.reduce((a, b) => {
    return [a[0] * b[0], a[1] * b[1]];}, [1, 1], f3))[1]);





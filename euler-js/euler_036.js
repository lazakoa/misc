/*
Problem 36: Double-base palindromes

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
*/

var wu = require('wu');

function reverseStr(s) {
    return s.split('').reverse().join('');
}

function stripLeading(s, ch) {
    var temp = s.split('');
    while(temp[0] === ch) {
        temp.shift();
    }
    return temp.join('');
}

function isPalindromic(s) {
    return s === stripLeading(reverseStr(s), '0');
}

function isValid(x) {
    return isPalindromic(x.toString()) && isPalindromic(x.toString(2));
}

function* rangeIter(start, end) {
    for (var counter = start; counter < end; counter ++) {
        yield counter;
    }
}    

var total = wu(wu(rangeIter(1, 
                    10**6 + 1)).filter(isValid)).reduce( (a, b) => a + b);

console.log(total);

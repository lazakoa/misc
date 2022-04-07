/*
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

var upperBound = 999*999;
var lowerBound = 100*100;

function possibleList(x) {
    function uB(x) {
        // helper for upper bound
        var temp = "";
        for (var counter = 0; counter < x; counter++) {
            temp += '9';
        }
        return Number(temp);
    }

    function lB(x) {
        // helper for lower bound
        var temp = "1";
        for (var counter = 0; counter < x - 1; counter++) {
            temp = temp + "0";
        }
        return Number(temp);
    }
    
    var possible = [];
    for (var i = lB(x); i < uB(x); i++) {
        for (var j = lB(x); j < uB(x); j++) {
                possible.push(i*j);
        }
    }
    return possible;
}

function isPalindrome(x) {
    return revStr(x) === String(x);
}

function revStr(x) {
    return String(x).split("").reverse().join("");
}

function aGtb(a, b) {
    if (a > b) {
        return a;
    }
    else {
        return b;
    }
}

function filter(f, array) {
    var temp = [];
    for (var counter = 0; counter < array.length; counter++) {
        if (f(array[counter]))
            temp.push(array[counter]);
    }
    return temp;
}

console.log(filter(isPalindrome, possibleList(3)).reduce(aGtb));









 

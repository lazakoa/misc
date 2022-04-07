/*
Problem 39: Integer right triangles

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
*/

// restated as which perimeter p < 1000 can form the greatest number of valid
// right triangles. Find this p.

// n/2 + 1 + sqrt(1 + n^2/4) = n

// generate all triplets {a, b, c} st a + b + sqrt(a^2 + b^2) = n
// need to generate a permutation of 2 with lower bound 1 & upper bound of p - 1
// upper bound reduced to n/2 - 1, lower bound is still 1


// a + b + sqrt(a^2 + b^2) = n
// (n - a - b)^2 = a^2 + b^2

var G = require('generatorics');
var wu = require('wu');
var lo = require('lodash');

function* rangeIter(start, end) {
    for (var counter = start; counter < end; counter ++) {
        yield counter;
    }
}    

function isValidPerim(a, p) {
    return (p - a[0] - a[1])**2 === (a[0]**2 + a[1]**2);
}

function countSolutions(p) {
    var total = 0;
    const anon = (x) => isValidPerim(x, p);
    var temp = wu(G.combination(lo.range(1, Math.ceil(p/2)), 2)).filter(
                   anon);
    wu(temp).reduce((a, b) => total++, 0);
    return total;
}

// this can be made much faster, i don't need to generate the 
// combination over and over, just do it once for the max val of p  and 
// reuse it in find max, count solutions is seperate as an artifact of how I 
// did this. it works so I don't care for now.

function findMax(p) {

    var max = {perimeter: 0, total: 0}; 
    var temp;
    for (var counter = 3; counter < p; counter++) {
        temp = countSolutions(counter);
        if (temp > max.total) {
            max.perimeter = counter;
            max.total = temp;
        }
    }
    return max.perimeter;
}

console.log(findMax(1000));


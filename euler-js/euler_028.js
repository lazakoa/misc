/*
Problem 28: Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
*/

// spiral goes clockwise

// there is a cute paper based way to do this one probably

var lo = require('lodash');

function diagonal(matrix) {
    // extracts the diagonal of a matrix composed of n arrays where each array
    // has n elements
    
    var temp = [];
    for (var i = 0;  i < matrix.length; i++) {
        temp.push(matrix[i][i]);
    }
    return temp;
}

// grid should *be* matrix, reused from 11

function transpose(grid) {
    // transposes an n-array of n-array
    var temp = lo.map(grid, (_ , index) => { return lo.map(grid,
                                        (array) => { return array[index]; });});
    return temp;
}    

function stuff() {
    // keeps stuffing things into other things as long as space is available
    return null;
}

/*
 * 1. add a border to a matrix
 * 2. force a random walk from a starting point & path is allowed only along 
 *    certain values + specify the minimum number of steps, keep walking until
 *    you can't go anymore. Return an iterable with the entire path.
 * 3.
 * 4. keep stuffing values into the *object* while there is space left.
 * 5. return the stuffed *object*
 *
 * Above would be fun, would take too much time to write.
 *
 */

function addBorder(matrix, n, unit) {
    // adds a n unit border to a matrix, matrix has to be 1x1 at the minimum
    // where a 1x1 matrix is defined as [[1]]
    
    var temp = lo.map(matrix, 
        (x) => { return clone(unit, n).concat(x).concat(clone(unit, n));});

    return [clone(unit, 
                 temp[0].length)].concat(temp).concat([clone(unit,
                                                           temp[0].length)]);
}

/*
 * 1x1 -> 3x3 -> 5x5 -> 7x7 -> 9x9
 *      21 22 23 24 25
 *      20  7  8  9 10
 *      19  6  1  2 11
 *      18  5  4  3 12
 *      17 16 15 14 13
 *   
 *      (25 9 1 5 17) (21 7 1 3 13)
 * every number nxn +
 *
 * (1)*2 + 4 numbers + 4 numbers + 4 numbers
 *
 * top right corner: 
 * n^2 
 *
 * top left corner:
 * n^2 -   (n - 1)
 *
 * bottom left corner:
 * n^2 - 2*(n - 1)
 *
 * bottom right corner:
 * n^2 - 3*(n - 1)
 *
 * find sum of diagonals in both directions.
 */

function diagonalSum(n) {
    if (n === 1) {
        return 2;
    }
    else {
        var temp = (4 * (n * n)) - (6 * (n - 1));
        return temp + diagonalSum(n - 2);
    }
}

// I didn't need all that other crap i wrote. I realized exactly how much extra
// work would have been needed using a random walk + iterators. 
console.log(diagonalSum(1001) - 1);

/*
function clone(elem, n) {
    var temp = [];
    for (var counter = 0; counter < n; counter++)
        temp.push(elem);
    return temp;
}
*/

/*
function makeSpiralMatrix(n) {

    // makes a nxn matrix that spirals in the clockwise direcition as so:
    //
    //                        21 22 23 24 25
    //                        20  7  8  9 10
    //                        19  6  1  2 11
    //                        18  5  4  3 12
    //                        17 16 15 14 13
    //
    function recur(matrix, counter, iterator) {
        if (counter === n) {
            return matrix;
        }
        else {
            return recur(
        }
    }
    return recur([[1]], counter + 1
    
}
*/


/*
Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

function range(start, end) {
    /* returns an array starting at start and terminating at end 
     */
    var temp = [];
    for (var counter = start; counter < end; counter++) {
        temp.push(counter);
    }
    return temp;
}

function sum(array) {
    /* sums an array of numbers
     */
    total = 0;
    for (var counter = 0; counter < array.length; counter++) {
        total += array[counter];
    }
    return total;
}

function filter(f, array) {
    var temp = [];
    for (var counter = 0; counter < array.length; counter++) {
        if (f(array[counter]))
            temp.push(array[counter]);
    }
    return temp;
}
console.log(sum(filter(function(x) { return x % 3 == 0 || x % 5 == 0;},
    range(1, 1000))));

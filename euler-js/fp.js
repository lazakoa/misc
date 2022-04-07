
/* A homebrewed library for functional programming. 
 *
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

function map(f, array) {
}



/*
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
*/

/*
 * This can be quickly computed by hand. I'm not interested in doing that.
 */

var lo = require('lodash');

function generate(y) {
    // starting at a multiple of all the primes would be faster.
    var counter = y;
    while (!(lo.filter(lo.range(1,y + 1), function(x) {
        return counter % x === 0;}).length === y)) {
        counter++;
    }
    return counter;
}

console.log(generate(20));





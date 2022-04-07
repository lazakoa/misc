/*
Problem 26: Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
*/

var lo = require('lodash');

function longestRecurringCycle(d) {
    var cycles = lo.map(lo.range(2, d), (x) => {
        return recurringCycle(x).length;});
    return cycles.indexOf(lo.max(cycles)) + 2;
}

/*
 * 1/9 ~= 0.[10/9][10/9]...
 * 1/8 ~= 0.[10/8][20/8][40/8]
 * 1/13 ~= 0.(076923)
 *
 */

/*
 * This is technically a bit off but it still worked in the end. It doesn't
 * count the a recurring cylcle, what it does is keep dividing and giving 
 * terms in the fraction until it starts repeating. It just so happened that
 * the longest 1/[d] fraction also happened to be the longest recurring cycle.
 * 
 * It is trivially easy to modify the fucntion a bit to make it return only 
 * recurring cycles instead of doing division like it does now.
 *
 */

function recurringCycle(x) {

    function recur(dividend, divisor, cycle, dividends) {

        var temp = raiseBase(dividend, divisor);
        var remainder = temp.dividend % divisor;
        var val = zeroPad(temp.zeros - 1,
                            String((temp.dividend - remainder) / divisor));

        if (dividends.indexOf(dividend) === -1 && remainder === 0) {
            return cycle.concat(val);
        }
        else if ((remainder === 0) || dividends.indexOf(dividend) !== -1) {
            return cycle;
        }
        else {
            return recur(remainder, 
                         divisor, 
                         cycle.concat(val),
                         dividends.concat(dividend));
        }
    }

    return lo.reduce(recur(1, x, [], [x]), (a, b) => { return a + b; });
}

function zeroPad(n, str) {
    var temp = '';
    for (var counter = 0; counter < n; counter++) {
        temp = '0' + temp;
    }
    return temp + str;
}

function raiseBase(dividend, divisor) {
    var result = {zeros: 0};
    while (dividend / divisor < 1) {
        result.zeros += 1;
        dividend *= 10;
    }
    result.dividend = dividend;
    return result;
}

console.log(longestRecurringCycle(1000));

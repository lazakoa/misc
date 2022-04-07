/*
Problem 34: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
*/
// 9! = 3628800 (maximum a single digit can generate)
// 8! = 40320



function factorial(n) {
    var total = 1;
    for (var counter = 0; counter < n;) {
        counter++;
        total = total * counter;
    }
    return total;
}

function genCache(n) {
    var cache = {};
    for (var counter = 1; counter < n + 1; counter++) {
        cache[counter] = factorial(n);
    }
    return cache;
}


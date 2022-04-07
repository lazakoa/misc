/*
Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
*/

function nextPrime(x) {
    // Takes a number and returns the next prime number after it.
    x += 1;
    while (checkPrime(x) == false) {
        x += 1;
    }
    return x;
}

function checkPrime(x) {
    if (x === 1) {
        return false;
    }
    else {
        for (var counter = 2; counter * counter <= x; counter++) {
            if ( x % counter === 0) 
                return false;
        }
    }
    return true;
}

function primeList(n) {
    // generates a list of n prime numbers
    var temp = [2];
    while (temp.length != n) {
        temp.push(nextPrime(temp[temp.length - 1]));
    }
    return temp;
}

var ans = primeList(10001);

console.log(ans[ans.length - 1]);


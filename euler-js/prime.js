
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

module.exports.checkPrime = checkPrime;

function nextPrime(x) {
    // Takes a number and returns the next prime number after it.
    x += 1;
    while (checkPrime(x) == false) {
        x += 1;
    }
    return x;
}

module.exports.nextPrime = nextPrime;

function primeList(n) {
    // generates a list of n prime numbers
    var temp = [2];
    while (temp.length != n) {
        temp.push(nextPrime(temp[temp.length - 1]));
    }
    return temp;
}

module.exports.primeList = primeList;

function decompose(x) {
    // decomposes x into a array of prime factors, will show repeat factors
    var i = 2;
    var factors = [];
    while (i <= x) {
        while (x % i === 0) {
            factors.push(i);
            x = x / i;
        }
        i = nextPrime(i);
    }
    return factors;
}

module.exports.decompose = decompose;


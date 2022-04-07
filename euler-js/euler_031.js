/*
Problem 31: Coin sums

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
*/

// I'm pretty sure this is solvable with generating functions & sage. In
// fact it becomes trivial.

// tree never breaks a depth of 200, stack is safe
// this is very slow :(

// count these manually to reduce tree size
// 200  1
// 100 + 100 1
// 100 + countChange(100)
// countChange(200) (but no 100 & 200 piece)

// this didn't work, counts every possibility, duplicated are treated as unique
// too bad it was really pretty & fast
/*
function countChange(x) {
    const coins = [1, 2, 5, 10, 20, 50];
    var cache = {};
    function recur(n) {
        if (String(n) in cache) {
            return cache[n];
        }
        else if (n < 0) {
            return 0;
        }
        else if (n === 0) {
            cache[n] = 1;
            return 1;
        }
        else {
            var sum = 0;
            for (var coin of coins) {
                sum = sum + recur(n - coin);
                }
            }
            cache[n] = sum;
            return sum;
        }
    return recur(x);
}
*/

var lo = require('lodash');

function countChange(x) {
    const coins = [1, 2, 5, 10, 20, 50, 100, 200];
    // max number of allowed coins, this really should be dynamically
    // generated based on what x is
    const mCoins = {1:200, 2:100, 5:40, 10:20, 20:10, 50:4, 100:2, 200:1};

    function recur(coinCounts, indice) {
        // coinCounts is an array that represents 
        var totalChange = scalar(coinCounts, coins);

        if (totalChange === x) {
            return 1;
        }
        else if (totalChange > x) {
            return 0;
        }
        else if (indice === coins.length) {
            // first if will have gotten indice = 8 & total is x
            return 0;
        }
        else {
            var sum = 0;
            var current = coins[indice];
            for (var counter = 0; counter < mCoins[current] + 1; counter++) {
                var temp = coinCounts.slice();
                temp[indice] = counter;
                sum = sum + recur(temp, indice + 1);
            }
            return sum;
        }
    }
    
    return recur([0,0,0,0, 0,0,0,0], 0);
}

function scalar(array1, array2) {
    // arrays have to be the same length
    var temp = [];
    for (var counter=0; counter < array1.length; counter++) {
        temp.push(array1[counter] * array2[counter]);
    }
    return lo.reduce(temp, (a, b) => { return a + b; });
}

// I'm on a roll, worked on the first try after beating out the syntax errors
// kinda slow, does a little extra work on some of the tree branches.
// maybe? i can stick a condition in the for loop to break out of it if the
// scalar product total has hit past x. Would the work saved by the condition
// check having been done each time be worth the gain? I shave of cycles off
// my for loop inside the recurrence at the cost of more for loops inside a
// check with scalar.

console.log(countChange(200));


/*
Problem 31: Coin sums

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
*/

// tree never breaks a depth of 200, stack is safe
// this is very slow :(

// count these manually to reduce tree size
// 200  1
// 100 + 100 1
// 100 + countChange(100)
// countChange(200) (but no 100 & 200 piece)

// this didn't work, counts every possibility, duplicated are treated as unique
// too bad it was really pretty
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

function countChange(x) {
    const coins = [1, 2, 5, 10, 20, 50, 100, 200];
    var maxCoins = [200, 100, 40, 20, 10, 4, 2, 1];

    recur(howmany) {
        var sum = scalar(howmany, coins);
        if (sum > x) {
            return 0;
        }
        else if (sum === x) {
            return 1;
        }
        else { 
            for (var counter = 0; counter < coins.length;) {
            }
        }
    }
    
    return recur([0,0,0,0, 0,0,0,0]);
}

function scalar(array1, array2) {
    // arrays have to be the same length
    var temp = [];
    for (var counter=0; counter < array1.length; counter++) {
        temp.push(array1[counter] * array2[counter]);
    }
    return lo.reduce(temp, (a, b) => { return a + b; });
}

// lock coin# 1 in place -> 
// lock coin# 2 in place ->
// lock coin# 3 in place ->
// lock coin# 4 in place ->
// ...
// lock coin# 8 in place ->
// check if sum matches what we want

// need to count the number of unique arrangements [a1*1, a2*2, ... ] 
// where the sum of the array is equal to 200

console.log(countChange(200));

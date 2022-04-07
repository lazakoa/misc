/*
Problem 38: Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
*/

var wu = require('wu');

function* maskMaker() {
    var temp = [];
    var counter = 1;
    while (true) {
        temp.push(counter);
        counter++;
        yield temp;
    }
}

function isPandigital(x) {
    // takes a number that has been converted to a string
    if (x.length !== 9) {
        return false;
    }
    var temp2 = new Set(x.split(''));
    
    if (temp2.has('0')) {
        return false;
    }
    else {
        if (temp2.size === 9) {
            return true;
        }
        else {
            return false;
        }
    }
}

function* rangeIter(start, end) {
    for (var counter = start; counter < end; counter ++) {
        yield counter;
    }
}    

function concatProduct(number) {
    var temp = wu(maskMaker()).map( x => x.map( y => y * number).join(''));
    var f1 = wu(wu(temp).takeWhile(
        x => x.length <= 9)).filter(isPandigital);
    
    var res = [];
    for (var item of f1) {
        res.push(Number(item));
    }
    return res;
}

// got it on the first try yay! I'm getting more careful now. This was kinda
// easy :(

console.log(wu(wu(rangeIter(1, 100000)).map(concatProduct)).reduce( (a, b) =>
    { return a.concat(b); }).reduce( (a, b) => {
        if (a > b) {
            return a;
        }
        else {
            return b;
        }
    }));



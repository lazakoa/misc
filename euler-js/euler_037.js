/*
Problem 37: Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
*/

/* 2, 3, 5, 7 are our base cases
 */

var prime = require('./prime.js');
var wu = require('wu');
var lo = require('lodash');

// This thing is pretty fucking fast actually, takes about a second to solve
// the question. Entire solution was "designed" on paper, more moving parts
// in there than i'm used too, plus i had to set up the filters to eliminate
// redundant work.

// Kinda ugly, but I didn't know how much work I would be doing up front
// to find the 11 primes, so i made it go as fast as I could think of with
// minimal effort. Uses like no memory too.

function euler37() {
   
   // valid first & last digits
   var fD = new Set([ '2', '3', '5', '7']);
   var lD = new Set([ '3', '7']);

   var primeCache = new Set();
    
   // works, saves a ton of work too
   var source = wu(wu.count(8)).filter( x => {
       return fD.has(x.toString()[0]) && lD.has(x.toString().slice(-1)); }
   );

   function isTruncatblePrime(x) {
       return smearOut(x).every( x => {
           if (primeCache.has(x)) {
               return true;
           }                    
           else if (prime.checkPrime(x)) {
               primeCache.add(x);
               return true;
           }
           else {
               return false;
           }
       });
   }

   var res = wu(wu(source).filter( x => {
       if (prime.checkPrime(x)) {
           primeCache.add(x);
           return true;
       }
       else {
           return false;
       }
   })).filter(isTruncatblePrime);

   var ans = 0;

   // woops, had 12 there after i finished the question to test memory usage
   for (var p of wu(res).take(11)) {
       ans += p;
   }
   return ans;
}

function smearOut(x) {
    var temp = String(x).split('');
    var rToL = temp.slice();
    var lToR = temp.slice();
    var result = []; 

    for (var counter = 0; counter < temp.length - 1; counter++) {
        rToL.shift();
        lToR.pop();
        result.push(Number(rToL.join('')));
        result.push(Number(lToR.join('')));
    }
    return result;
}

// Got the answer on first try! Yay.
console.log(euler37());

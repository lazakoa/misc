#!/bin/env node
/*
Problem 60: Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
*/

/* No way you can check all the combinations.
 *
 * Define concat(a,b) to be a function that returns a tuple s.t the first
 * element of the tuple is the digits of b appened to the end of the digits
 * of a, and vice versa for the second element of the tuple.
 *
 * concat(a,b) is equivalent to a*(10**(digits(b))) + b and 
 * b*(10**(digits(a))) + a.
 *
 * Definition of remarkable:
 * A set of primes called P is said to be remarkable if for every pi,pj s.t
 * pi != pj and where every element in the tuple concat(pi,pj) is prime. If 
 * there are n primes in the set P then there are combination(n,2) possible 
 * pairs pi, pj s.t pi != pj.
 *
 * Take pi, pj from the set P s.t pi != pj. If concat(pi,pj) then 
 * digits(concat(pi,pj)) = digits(pi) + digits(pj).
 *
 * Assume that the set P is drawn from a set P' s.t P' consists of all primes
 * p < b for some positive natural number b. combination(Ord(P'), Ord(P)) 
 * gives an upper bound on the total number of sets P that are possible.
 *
 * There are 168 primes s.t p < 1000.
 * There are 1229 primes s.t p < 10000.
 *
 * The sum of five primes that satisfy this property is less than or equal
 * to ~70million.
 *
 * 1. Can't be solved by brute force easily (possible, not recommended)
 * 2. Doing a tree search to generate all possible 5 prime solutions is not
 * feasible even for a low number of primes to search over. Also it is not 
 * known when convergence will occur. Set of primes is picked manually, (all
 * I need is an upper bound).
 *
 * Idea:
 * Let the set P be all primes less than or equal to some n. Where n is chosen
 * arbitrarily. Generate all pairs pi,pj E P s.t pi != pj. Filter out all the
 * pairs pi,pj that are not remarkable. *Somehow* chain together k pairs s.t
 * (pi1,pj1) --> .... -> (pik,pjk) is remarkable when only the unique pi's and
 * pj's are considered.
 *
 * Steps:
 * 1. Generate a set of primes, with a upperbound p. (p is user configurable)
 * 2. Generate all pair wise combinations from the above set of primes.
 * 3. Filter out all pairs that are not remarkable.
 * 4. From the filtered pairs make a hash map where the keys are primes
 * and the value associated with each is a set of primes that form remarkable
 * pairs with the key.
 * 5. Do a tree search to find all possible solutions of length k (k is
 * a configurable parameter).
 * 6. If there are no answers set p to be higher and run this again. 
 *
 * Very similar to one of the later questions I had solved in python. (one of
 * the 60's)
 * 
 * If the above doesn't work then give up and think up a new approach.
 */

var pri = require('primality');
var lo = require('lodash');
var G = require('generatorics');
var wu = require('wu');

function primes(n) {
    /* generates all primes p < n
    */
    return lo.filter(lo.range(0, n + 1), pri.primality); 
}

function search(n, k) {
    /* n is the bound for the set of primes we are using
     * k denotes the size of the set which is remarkable.
     * function finds all possible sets of size k given all primes up to n.
     */
    var pset = primes(n);
    var pairs = remarkablePairs(pset);

    var solutions = [];
    // Makes a whole bunch of redundant copies of solutions, still fast enough
    // to compute answer in a few seconds. Not optimizing this, looks like a
    // pain.
    function recur(l) {
        if (l.length === k) {
            //
            solutions.push(l);
            return l.slice(0,-1);
        } else if (l.length === 0) {
            for (var pair in pairs) {
                recur([Number(pair)]); // starts with length 1
            }
        } else {
            /* Loop over all keys in pairs
             */
            var temp = new Set(l);
            for (var elem of pairs[l.slice(-1)]) {
                // if the elem is already in the list, skip it
                if (!(temp.has(elem))) {
                    // check if elem occurs in every 
                    if (l.every((x) => {
                        return pairs[x].has(elem);})) {
                        recur(l.concat(elem));
                    }
                }
            }
            return l.slice(0,-1);
        }
        return 1;
    }
    recur([]);
    return solutions;
}

/* LOL. Just realized I have a graph below.
 */

function remarkablePairs(set) {
    /* Pairs grow O(n^2) also the cost of the primality check grows with n.
     * I assume the primality check is naive and the growth on it is O(n^.5).
     */
    var temp = wu(G.combination(set, 2)).filter((x) => {
        return remarkable(x[0], x[1]);});
    var final = {};
    for (var pair of temp) {
        if (pair[0] in final) {
            final[pair[0]].add(pair[1]);
        } else {
            final[pair[0]] = new Set([pair[1]]);
        }
        if (pair[1] in final) {
            final[pair[1]].add(pair[0]);
        } else {
            final[pair[1]] = new Set([pair[0]]);
        }
    }
    return final;
}

function remarkable(a,b) {
    var n1 = Number(String(a) + String(b));
    var n2 = Number(String(b) + String(a));
    return pri.primality(n1) && pri.primality(n2);
}

console.log(lo.sum(search(9000, 5)[0]));

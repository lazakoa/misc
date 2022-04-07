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
 * If the above doesn't work then give up and think up a new approach.
 */

var pri = require('primality');
var lo = require('lodash');



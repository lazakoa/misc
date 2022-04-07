#!/bin/env node
/*
Problem 54: Poker hands

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

  * High Card: Highest value card.
  * One Pair: Two cards of the same value.
  * Two Pairs: Two different pairs.
  * Three of a Kind: Three cards of the same value.
  * Straight: All cards are consecutive values.
  * Flush: All cards of the same suit.
  * Full House: Three of a kind and a pair.
  * Four of a Kind: Four cards of the same value.
  * Straight Flush: All cards are consecutive values of same suit.
  * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared (see
example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

Consider the following five hands dealt to two players:

        Hand   Player 1            Player 2              Winner
        1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
               Pair of Fives       Pair of Eights
        2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
               Highest card Ace    Highest card Queen
        3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
               Three Aces          Flush with Diamonds
               4D 6S 9H QH QC      3D 6D 7H QD QS
        4      Pair of Queens      Pair of Queens        Player 1
               Highest card Nine   Highest card Seven
               2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        5      Full House          Full House            Player 1
               With Three Fours    with Three Threes

The file poker.txt contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated
cards), each player's hand is in no specific order, and in each hand there
is a clear winner.

How many hands does Player 1 win?

This problem references the following resources:

poker.txt
*/

/*
 * 1.  High Card: Highest value card.
 *     - high card 1
 *     - high card 2
 *     - high card 3
 *     - high card 4
 *     - possible draw
 * 2.  One Pair: Two cards of the same value.
 *     - check rank of pairs
 *     - high card 1
 *     - high card 2
 *     - high card 3
 *     - possible draw
 * 3.  Two Pairs: Two different pairs.
 *     - check rank of pair 1
 *     - check rank of pair 2
 *     - check rank of high card
 *     - possible draw
 * 4.  Three of a Kind: Three cards of the same value.
 *     - score the triplet (clear winner)
 * 5.  Straight: All cards are consecutive values.
 *     - check score of entire hand
 *     - possible draw
 * 6.  Flush: All cards of the same suit.
 *     - check score of entire hand
 * 7.  Full House: Three of a kind and a pair.
 *     - check rank of three of a kind (clear winner)
 * 8.  Four of a Kind: Four cards of the same value.
 *     - check rank of four of a kind
 *     - check rank of high card
 * 9.  Straight Flush: All cards are consecutive values of same suit.
 *     - check highest ending rank
 * 10. Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
 *     - draw
 *
 * 1. Determine hand type.
 * 2. Assign a numerical score to the hand type.
 *      Score is a sequence of numbers
 */

var fs = require('fs');
var lo = require('lodash');

// Read in & format poker.txt
var s = 'resources/poker.txt';
var hands = fs.readFileSync(s, 'utf8');
hands = hands.split('\n');
hands = lo.map(hands, (x) => { 
    return x.slice(0, -1).split(' ');}).slice(0,-1);

cardValues = {  2  :  2 ,
                3  :  3 ,
                4  :  4 ,
                5  :  5 ,
                6  :  6 ,
                7  :  7 ,
                8  :  8 ,
                9  :  9 ,
                'T':  10,
                'J':  11,
                'Q':  12,
                'K':  13,
                'A':  14}

function score(hand) {
    /* The default lexicographic sort fucked me up initially. I'm not happy
     * with how this turned out.
     */
    var temp1 = count(hand);
    var temp2 = invert(temp1);
    var final = [];
    var iter = lo.map(Object.keys(temp2), Number).sort().reverse();
    for (var multi of iter) {
        var stage = [];
        for (var counter = 0; counter < multi; counter++) {
            stage = stage.concat(lo.map(temp2[multi], 
                Number));
        }
        final = final.concat(stage.sort((a, b) => a - b).reverse());
    }
    return final;
}

// I don't like it, but for 5 card hands this is pretty cheap.
function invert(obj) {
    var temp = {};
    for (var key in obj) {
        if (obj[key] in temp) {
            temp[obj[key]].push(key);
        } else {
            temp[obj[key]] = [key];
        }
    }
    return temp;
}

function count(hand) {
    var temp = {};
    for (var card of hand) {
        if (cardValues[card[0]] in temp) {
            temp[cardValues[card[0]]] += 1;
        }
        if (!(cardValues[card[0]] in temp)) {
            temp[cardValues[card[0]]] = 1;
        }
    }
    return temp;
}

/*
 * Need a array where occurences are counted as a,a,a,b,b,c but if a and b
 * occur the same number of times it a and b need to be sorted highest to 
 * lowest
 */

function nkind(array) {
    function f(hand) {
        var counts = invert(count(hand));
        var totals = Object.keys(counts);
        for (var digit of array) {
            if (!(totals.includes(String(digit)))) {
                return false;
            }
        }
        return true;
    }
    return f;
}

highcard = nkind([1]);
onepair = nkind([2]);

function twopair(hand) {
    var temp = invert(count(hand));
    if (2 in temp) {
        if (temp[2].length == 2) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

threekind = nkind([3]);
fullhouse = nkind([3,2]);
fourkind = nkind([4]);

p5s = ['5H', '5C', '5S', '7S', 'KD'];

p8s = ['2C', '2S', '8S', '8D', 'TD'];

function flush(hand){
    type = hand[0][1];
    for (var card of hand) {
        if (card[1] !== type) {
            return false;
        }
    }
    return true;
}

function hasAce(hand) {
    for (var card of hand) {
        if (card[0] !== 'A') {
            return false;
        }
    }
    return true;
}

function straight(hand){
    values = [];
    for (var card of hand) {
        values.push(cardValues[card[0]]);
    }
    values = values.sort((a, b) => a - b);
    start = values[0] - 1;
    for (var value of values) {
        start += 1;
        if (start !== value) {
            return false;
        }
    }
    return true;
}

function straightflush(hand) {
    if (straight(hand) && flush(hand)) {
        return true;
    } else {
        return false;
    }
}

function royal(hand) {

    if (hasAce(hand) && straightflush(hand)) {
        return true;
    } else {
        return false;
    }
}

handOrder = [ royal, straightflush, fourkind, fullhouse, flush, straight, 
    threekind, twopair, onepair, highcard];

function rankhand(hand) {
    return lo.map(handOrder, (x) => {
        if (x(hand) === true) {
            return score(hand);
        } else {
            return 0;
        }});
}

function cscore(s1, s2) {
    for (var i in s1) {
        if (s1[i] > s2[i]) {
            return 1;
        } else if (s2[i] > s1[i]) {
            return 2;
        }
    }
    return 3;
}

function comparehand(h1, h2) {
    var r1 = rankhand(h1);
    var r2 = rankhand(h2);
    // 3 outcomes, 'p1', 'p2', 'draw'
    for (var i in r1) {
        if (r1[i] !== 0 && r2[i] !== 0) {
            var winner = cscore(r1[i], r2[i]);
            if (winner === 1) {
                return 'p1';
            }
            else if (winner === 2) {
                return 'p2';
            }
            else {
                return 'draw';
            }
        } else if (r1[i] !== 0) {
            return 'p1';
        } else if (r2[i] !== 0) {
            return 'p2';
        } else {
            continue;
        }
    }
}

winners = lo.map(hands, x => {
    return [x, comparehand(x.slice(0,5), x.slice(5,))];});

console.log(winners.filter( (x) => {return x[1] === 'p1';}).length);


#!/bin/env node
/*
Problem 59: XOR decryption

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key. The
advantage with the XOR function is that using the same encryption key on
the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using cipher1.txt, a file containing the encrypted
ASCII codes, and the knowledge that the plain text must contain common
English words, decrypt the message and find the sum of the ASCII values
in the original text.

This problem references the following resources:

cipher1.txt
*/

var fs = require('fs');
var lo = require('lodash');
var G = require('generatorics');
//var prompt = require('prompt-sync');
var query = require('cli-interact').getYesNo;

// Reading in the data.
var path = 'resources/cipher1.txt';
var cipher = fs.readFileSync(path, 'utf8');
cipher = lo.map(cipher.slice(0,-2).split(','), Number);

function decrypt(cipher, key) {
    var temp = []; 
    var counter = 0;
    for (var code of cipher) {
        temp.push(code ^ key[counter]);
        counter = (counter + 1) % key.length;
    }
    return temp;
}

function search(cipher) {
    // approx 2 million possible keys
    var keys = G.permutation(lo.range(97,123), 3);
    var partial = cipher.slice(0,78);
    for (var key of keys) {
        var temp = decrypt(partial, key);
        temp = lo.map(temp, (x) =>
                String.fromCharCode(x)[0]).join('');
        console.log(temp, key);
    }
    return temp;
}

function undoASCII(cipher, key) {
    var temp = decrypt(cipher, key);
    var total = lo.sum(temp);
        temp = lo.map(temp, (x) =>
                String.fromCharCode(x)[0]).join('');
    //console.log(temp); // wanted to read the text :)
    return total;
}

// password from the procedure below
var pass = [103, 111, 100]

/* generated a text file and searched by visual inspection for common phrases.
 * Grep for 'the' and 'and'.
 */
//search(cipher);
//

console.log(undoASCII(cipher, pass));

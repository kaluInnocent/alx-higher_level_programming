#!/usr/bin/node

// A script that prints argument passed to it

const myarg = process.argv.slice(2);

if (myarg) {
console.log(myarg[0]);
} else {
console.log('No argument');
}

#!/usr/bin/node

// A script that prints argument passed to it

const myarg = process.argv;

if (myarg[2]) {
  console.log(myarg[2]);
} else {
  console.log('No argument');
}

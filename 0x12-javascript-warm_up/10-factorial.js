#!/usr/bin/node

/*
* A script that computes and prints a factorial
* The first argument is integer (argument can be cast as integer)
*  used for computing the factorial
*/

function myFact (n) {
  if (n <= 1) {
    return (1);
  } else {
    return (n * myFact(n - 1));
  }
}

const args = process.argv;
const num = parseInt(args[2]);

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(myFact(num));
}

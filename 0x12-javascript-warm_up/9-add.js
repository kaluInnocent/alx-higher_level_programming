#!/usr/bin/node

/*
 * script pribts the addition of two numbers
 * The first argument is the first integer
 * The second argument is the second integer
 */

function add (a, b) {
  return (a + b);
}

 const args = process.argv;

if ((args.length <= 3) || isNaN(parseInt(args[2])) || isNaN(parseInt(args[3]))) {
  console.log('NaN');
} else {
  const a = parseInt(args[2]);
  const b = parseInt(args[3]);
  console.log(add(a, b));
}

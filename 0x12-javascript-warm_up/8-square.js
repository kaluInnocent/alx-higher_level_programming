#!/usr/bin/node

/*
 * Write a script that prints a square
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer,
 * print “Missing number of occurrences”
 */

const args = process.argv;
const num = parseInt(args[2]);

if ((args.length === 2) || isNaN(num)) {
  console.log('Missing size');
} else {
  if (num < 0) {
  } else {
    for (let i = 0; i < num; i++) {
      console.log('X'.repeat(num));
    }
  }
}

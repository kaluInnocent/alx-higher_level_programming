#!/usr/bin/node

/*
 * Write a script that prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer,
 * print “Missing number of occurrences”
 */

const args = process.argv;

if (args.lenght === 2)  || (isNaN(parseInt(args[2]))) {
  console.log('Missing number of occurrences');
} else {
  if (parseInt(args[2]) < 0) {
    ;
  } else {
    for (const num = 0; num < parseInt(args[2]); num++) {
      console.log('C is fun');
    }

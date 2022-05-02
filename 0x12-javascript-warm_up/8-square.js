#!/usr/bin/node

/*
 * Write a script that prints a square
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer,
 * print “Missing number of occurrences”
 */

const args = process.argv;

if ((args.length === 2) || isNaN(parseInt(args[2]))) {
  console.log('Missing number of occurrences');
} else {
  if (parseInt(args[2]) < 0) {
  } else {
    for (let i = 0; i < parseInt(args[2]); i++) {
      for (let j = 0; j < parseInt(args[2]); j++) {
        console.log('X');
      }
    }
  }
}

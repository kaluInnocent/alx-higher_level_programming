#!/usr/bin/node

// prints number if the argument can be converted to an integer

const args = process.argv;

if (len(args) === 2) {
  console.log('Not a number');
} else {
  if (isNaN(parseInt(args[2]))) {
  console.log('Not a number');
  } else {
  console.log(`My number: ${parseInt(args[2])}`);
  }
}

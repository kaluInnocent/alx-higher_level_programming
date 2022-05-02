#!/usr/bin/node
const process = require('process');

// print process.argv
if (process.argv.length - 2 > 1) {
  console.log('Arguments found');
} else if (process.argv.length - 2 === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}

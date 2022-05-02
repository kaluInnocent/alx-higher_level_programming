#!/usr/bin/node

const process = require('process');
const arg = process.argv.slice(2); 
if (arg[0] === null){
console.log('No argument');
} else{
console.log(arg[0]);
}

#!/usr/bin/node

Const process = require('process');
Const arg = process.argv.slice(2);
if (arg[0] === null){
console.log('No argument');
} else{
console.log(arg[0]);
}

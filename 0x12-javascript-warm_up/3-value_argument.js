#!/usr/bin/node

Const process = require('process');
if (process.argv[2] === null){
console.log('No argument');
} else{
console.log(process.argv[2]);
}

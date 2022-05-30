#!/usr/bin/node

const file = require('file');
const arg1 = file.readFileSync(process.argv[2], 'utf8');
const arg2 = file.readFileSync(process.argv[3], 'utf8');
file.writeFileSync(process.argv[4], arg1 + arg2);

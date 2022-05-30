#!/usr/bin/node

const list = require('./100-data.js').list;
const array = list.map((y, idx) => { return y * idx; });
console.log(list);
console.log(array);

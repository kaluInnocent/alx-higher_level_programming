#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];
  for (let idx = list.length - 1; idx >= 0; idx--) {
    arr.push(list[idx]);
  }
  return arr;
};

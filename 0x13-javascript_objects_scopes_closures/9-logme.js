#!/usr/bin/node

exports.logMe = (function (item) {
  let count = 0;
  return (item) => console.log(`${count++}: ${item}`);
})();

#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const eleCount = {};
  for (let idx = 0; idx < list.length; idx++) {
    eleCount[list[idx]] = 1 + (eleCount[list[idx]] || 0);
  }
  return eleCount[searchElement];
};

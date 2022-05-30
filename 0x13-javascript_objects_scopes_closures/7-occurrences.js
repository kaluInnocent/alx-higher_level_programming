#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const eleCount = {};
  for (let idx = 0; idx < list.length; idx++) {
    eleCount[list[idx]] = 1 + (eleCount[list[idx]] || 0);
  }
  if (list.includes(searchElement) && list.some(() => list[list.indexOf(searchElement)] ===
 searchElement)) {
    return eleCount[searchElement];
  }
  return 0;
};

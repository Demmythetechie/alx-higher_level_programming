#!/usr/bin/node

// This script returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let occr = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occr += 1;
    }
  }
  return occr;
};

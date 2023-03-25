#!/usr/bin/node
exports.esrever = function (list) {
  let rev = [];
  for (let i = list.length - 1, x = 0; i >= x; i--) {
    rev.push(list[i]);
  }
  return rev
};

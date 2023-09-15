#!/usr/bin/node

const lists = require('./100-data.js').list;
// This script imports an array and computes a new array

console.log(lists);
lists.map(function (list, index) {
  list = list * index;
  lists[index] = list;
  return lists;
});
console.log(lists);

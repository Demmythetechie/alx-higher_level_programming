#!/usr/bin/node

// This script returns the reversed version of a list

exports.esrever = function (list) {
  const nList = [];
  for (let i = 0; i < list.length; i++) {
    nList.unshift(list[i]);
  }
  return nList;
};

#!/usr/bin/node

// This script prints the addition of 2 integers

function add (a, b) {
  console.log(a + b);
}

add(Number(process.argv[2]), Number(process.argv[3]));

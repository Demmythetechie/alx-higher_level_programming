#!/usr/bin/node
const argv = process.argv;
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(Number(a) + Number(b));
  }
}

add(argv[2], argv[3]);

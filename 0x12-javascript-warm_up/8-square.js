#!/usr/bin/node

// This script prints a square

if (Number(process.argv[2])) {
  let x = '';
  for (let i = 0; i < Math.floor(Number(process.argv[2])); i++) {
    for (let i = 0; i < Math.floor(Number(process.argv[2])); i++) {
      x += 'X';
    }
    if (i < Math.floor(Number(process.argv[2])) - 1) {
      x += '\n';
    }
  }
  console.log(x);
} else {
  console.log('Missing size');
}

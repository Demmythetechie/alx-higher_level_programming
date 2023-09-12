#!/usr/bin/node

// This script prints x times “C is fun”

if (Number(process.argv[2])) {
  for (let i = 0; i < Math.floor(process.argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

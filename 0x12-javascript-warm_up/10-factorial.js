#!/usr/bin/node

// This script computes and prints a factorial

function factorial (num, rst) {
  if (process.argv[2] === undefined) {
    console.log(rst);
    return rst;
  }
  if (num === 1) {
    console.log(rst);
    return rst;
  }
  rst *= num;
  factorial(num - 1, rst);
}

factorial(Number(process.argv[2]), 1);

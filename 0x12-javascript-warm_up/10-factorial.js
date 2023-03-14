#!/usr/bin/node

function factorial (c = Number(process.argv[2])) {
  let fac = 1;
  if (isNaN(c) || c === undefined) {
    console.log(fac);
  } else {
    for (let i = 1; i <= c; i++) {
      fac *= i;
    }
    console.log(fac);
  }
}

factorial();

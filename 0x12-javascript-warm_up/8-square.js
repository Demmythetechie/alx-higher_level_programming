#!/usr/bin/node
const argv = process.argv;
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let row = 0; row < argv[2]; row++) {
    let r = '';
    for (let col = 0; col < argv[2]; col++) {
      r = r + 'X';
    }
    console.log(r);
  }
}

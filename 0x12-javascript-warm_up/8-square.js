#!/usr/bin/node

let str = 'Missing size';
if (Number(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    str = '';
    for (let i = 0; i < process.argv[2]; i++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log(str);
}

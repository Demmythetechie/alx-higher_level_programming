#!/usr/bin/node

const arg = [];
for (let i = 2; i < process.argv.length; i++) {
  arg.push(Number(process.argv[i]));
}
if (arg.length <= 1) {
  console.log(0);
} else {
  arg.sort(function (a, b) { return b - a; });
  console.log(arg[1]);
}

#!/usr/bin/node
let argv = process.argv;
if (argv.length <= 3) {
  console.log('0');
} else {
  argv = argv.slice(2, argv.length);
  argv = argv.map(Number);
  argv.sort(function (a, b) {
    return b - a;
  });
  console.log(argv[1]);
}

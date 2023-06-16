#!/usr/bin/node
const argv = process.argv;
if (argv.length <= 3) {
  console.log('0');
} else {
  argv.sort();
  console.log(argv);
  console.log(argv[argv.length - 1]);
}

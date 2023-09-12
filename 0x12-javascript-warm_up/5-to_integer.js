#!/usr/bin/node

/*
 * This script prints My number: <first argument converted in integer>
 *  if the first argument can be converted to an integer
 */

if (Number(process.argv[2])) {
  console.log(Math.floor(Number(process.argv[2])));
} else {
  console.log('Not a number');
}

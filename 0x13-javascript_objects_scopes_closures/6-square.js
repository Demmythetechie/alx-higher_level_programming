#!/usr/bin/node
const Squares = require('./5-square.js');
/* This scriipt creates a class Square that defines a square
 * and inherits from Rectangle of 4-rectangle.js
 */

class Square extends Squares {
  charPrint (c) {
    this.print(c);
  }

  print (c) {
    if (c === undefined) {
      c = 'X';
    }
    let shape = '';
    for (let ht = 1; ht <= this.height; ht++) {
      for (let wt = 1; wt <= this.width; wt++) {
        shape += c;
      }
      if (ht !== this.height) {
        shape += '\n';
      }
    }
    console.log(shape);
  }
}

module.exports = Square;

#!/usr/bin/node

// This script creates an empty class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let shape = '';
    for (let ht = 1; ht <= this.height; ht++) {
      for (let wt = 1; wt <= this.width; wt++) {
        shape += 'X';
      }
      if (ht !== this.height) {
        shape += '\n';
      }
    }
    console.log(shape);
  }
}

module.exports = Rectangle;

#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        str += 'X';
      }
      if (i !== this.height - 1) {
        str += '\n';
      }
    }
    console.log(str);
  }

  rotate () {
    const exch = this.width;
    this.width = this.height;
    this.height = exch;
  }

  double () {
    this.width = this.width ** 2;
    this.height = this.height ** 2;
  }
};

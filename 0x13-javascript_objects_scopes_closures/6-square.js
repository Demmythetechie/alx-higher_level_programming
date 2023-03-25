#!/usr/bin/node
const Squaree = require('./5-square.js')

module.exports = class Square extends Squaree {
  charPrint(c='X') {
    super.print(c)
  }
}

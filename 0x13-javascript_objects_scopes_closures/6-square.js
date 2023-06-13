#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let str = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          str += c;
        }
        if (i < this.height - 1) {
          str += '\n';
        }
      }
      console.log(str);
    }
  }
}

module.exports = Square;

#!/usr/bin/node

exports.logMe = function (item) {
  if (this.n === undefined) {
    this.n = 0;
  }
  console.log(`${this.n}: ${item}`);
  this.n++;
};

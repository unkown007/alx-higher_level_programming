#!/usr/bin/node

const dict = require('./101-data').dict;

const tmp = {};
for (const x in dict) {
  if (tmp[dict[x]] === undefined) {
    tmp[dict[x]] = [];
  }
  tmp[dict[x]].push(x);
}
console.log(tmp);

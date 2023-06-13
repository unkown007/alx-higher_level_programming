#!/usr/bin/node

const fs = require('fs');

let data = '';
try {
  data = fs.readFileSync(process.argv[2], 'utf8');
} catch (err) {
  console.error(err);
}
try {
  data += fs.readFileSync(process.argv[3], 'utf8');
} catch (err) {
  console.error(err);
}
try {
  fs.writeFileSync(process.argv[4], data);
} catch (err) {
  console.error(err);
}

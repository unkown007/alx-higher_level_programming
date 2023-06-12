#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  let sqr = '';
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      sqr += 'X';
    }
    if (i < parseInt(process.argv[2]) - 1) {
      sqr += '\n';
    }
  }
  console.log(sqr);
}

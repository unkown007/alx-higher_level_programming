#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let max = parseInt(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
    if (max < parseInt(process.argv[i])) {
      max = parseInt(process.argv[i]);
    }
  }
  let smax = -Number.MIN_VALUE;
  let n = 0;
  for (let i = 2; i < process.argv.length; i++) {
    n = parseInt(process.argv[i]);
    if (smax < n && n < max) {
      smax = n;
    }
  }
  console.log(smax);
}

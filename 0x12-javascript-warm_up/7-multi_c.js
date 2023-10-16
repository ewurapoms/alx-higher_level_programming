#!/usr/bin/node
const m = Math.floor(Number(process.argv[2]));
if (isNaN(m)) {
  console.log('Missing number of occurrences');
} else {
  for (let n = 0; n < m; n++) {
    console.log('C is fun');
  }
}

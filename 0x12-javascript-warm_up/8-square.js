#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let width = 0; width < size; width++) {
    let shape = '';
    for (let height = 0; height < size; height++) shape += 'X';
    console.log(shape);
  }
}

#!/usr/bin/node
function bigInt (arr) {
  let max = 0; let sum = 0;

  for (const val of arr) {
    const num = Number(val);

    if (num > max) {
      [sum, max] = [max, num];
    } else if (num < max && num > sum) {
      sum = num;
    }
  }

  return sum;
}

console.log(bigInt(process.argv));

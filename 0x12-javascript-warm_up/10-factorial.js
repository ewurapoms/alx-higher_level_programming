#!/usr/bin/node
function factorial (f) {
  return f === 0 || isNaN(f) ? 1 : f * factorial(f - 1);
}

console.log(factorial(Number(process.argv[2])));

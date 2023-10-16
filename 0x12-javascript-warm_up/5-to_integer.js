#!/usr/bin/node
const intArg = Math.floor(Number(process.argv[2]));
console.log(!isNaN(intArg) ? `My number: ${intArg}` : 'Not a number');

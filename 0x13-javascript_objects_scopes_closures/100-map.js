#!/usr/bin/node
// Import an array and compute a new array
const oldlist = require('./100-data').list;
const newlist = oldlist.map((v, i) => v * i);
console.log(oldlist);
console.log(newlist);

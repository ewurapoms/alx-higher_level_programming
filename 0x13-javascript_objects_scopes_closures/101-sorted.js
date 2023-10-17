#!/usr/bin/node
// imports and compute a dictionary of user ids by occurrence
const dict = require('./101-data.js').dict;

const sum = Object.entries(dict);
const value = Object.values(dict);
const specialV = [...new Set(value)];
const newDict = {};
for (const i in specialV) {
  const list = [];
  for (const key in sum) {
    if (sum[key][1] === specialV[i]) {
      list.unshift(sum[key][0]);
    }
  }
  newDict[specialV[i]] = list;
}
console.log(newDict);

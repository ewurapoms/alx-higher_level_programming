#!/usr/bin/node
let sum = 0;

exports.logMe = function (item) {
  console.log(sum + ': ' + item);
  sum++;
};

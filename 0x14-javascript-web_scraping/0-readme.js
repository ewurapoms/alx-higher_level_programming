#!/usr/bin/node
const argFile = process.argv[2];
const fs = require('fs');
fs.readFile(argFile, 'utf8', (error, data) => {
  if (error) {
    console.error('Error reading file:', error);
    return;
  }
  console.log(data);
});

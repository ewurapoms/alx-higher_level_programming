#!/usr/bin/node

const fs = require('fs');
const argFile = process.argv[2];
const text = process.argv[3];

fs.writeFile(argFile, text, 'utf-8', function (error) {
  if (error) console.log('Error reading file:', error);
});

#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const data = process.argv[3];

request(URL, function (error, response, body) {
  if (error == null) {
    fs.writeFileSync(data, body);
  }
});

#!/usr/bin/node

const request = require('request');
const argFile = process.argv[2];

request(argFile, function (error, response) {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});

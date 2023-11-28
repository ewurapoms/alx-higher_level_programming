#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
request(URL, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    const charWedge = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.includes('18'))
        ? count+ 1
        : count;
    }, 0);
    console.log(charWedge);
  }
});

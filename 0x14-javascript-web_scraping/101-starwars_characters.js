#!/usr/bin/node

const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(URL, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    starsList(characters, 0);
  }
});

function starsList (characters, position) {
  request(characters[position], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (position + 1 < characters.length) {
        starsList(characters, position + 1);
      }
    }
  });
}

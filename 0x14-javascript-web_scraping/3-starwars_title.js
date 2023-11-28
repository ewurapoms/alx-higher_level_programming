#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const API = 'https://swapi-api.hbtn.io/api/films/';

request(API + movieId, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const content = JSON.parse(body);
    console.log(content.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});

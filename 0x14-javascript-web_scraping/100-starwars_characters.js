#!/usr/bin/node

const request = require('request');
const file = process.argv[2];
const API = 'https://swapi-api.hbtn.io/api/films/';
request(API + file, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const list = JSON.parse(body);
  const print = list.characters;
  for (const c of print) {
    request(c, function (error, response, body1) {
      if (error) {
        console.error(error);
      }
      const newList = JSON.parse(body1);
      console.log(newList.name);
    });
  }
});

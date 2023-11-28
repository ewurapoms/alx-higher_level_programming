#!/usr/bin/node

const request = require('request');
const API = process.argv[2];
const taskList = {};

request(API, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in taskList)) {
          taskList[userid] = 0;
        }
        taskList[userid] += 1;
      }
    });
    console.log(taskList);
  }
});

#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error:', error);
    return;
  }
  const results = JSON.parse(body);
  const tasks = {};
  for (let i = 0; i < results.length; i++) {
    const key = results[i].userId.toString();
    if (results[i].completed) {
      if (tasks[key]) {
        tasks[key]++;
      } else {
        tasks[key] = 1;
      }
    }
  }
  console.log(tasks);
});

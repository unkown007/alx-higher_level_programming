#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error: ', error);
    return;
  }
  const results = JSON.parse(body);
  let size = 0;
  const tasks = {};
  for (let i = 0; i < results.length;) {
    let count = 0;
    const userId = results[i].userId;
    while (size < results.length && userId === results[size].userId) {
      if (results[size].completed) {
        count++;
      }
      size++;
    }
    i = size;
    if (count !== 0) {
      tasks[`${userId}`] = count++;
    }
  }
  console.log(tasks);
});

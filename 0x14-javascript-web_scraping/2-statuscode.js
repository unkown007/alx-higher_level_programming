#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error: ', error);
    return;
  }
  console.log('code:', response.statusCode);
});

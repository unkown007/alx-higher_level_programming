#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error:', error);
    return;
  }
  const results = JSON.parse(body).results;
  let count = 0;
  results.forEach((film) => {
    const characters = film.characters;
    characters.forEach((character) => {
      if (character.endsWith('18/')) {
        count++;
      }
    });
  });
  console.log(count);
});

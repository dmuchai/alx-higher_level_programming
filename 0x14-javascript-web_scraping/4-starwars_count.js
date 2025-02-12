#!/usr/bin/node
// Script that prints the number of movies where the character "Wedge Antilles" (ID 18) is present.

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';
let count = 0;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.forEach(movie => {
      if (movie.characters.some(character => character.includes(`/people/${characterId}/`))) {
        count++;
      }
    });
    console.log(count);
  }
});

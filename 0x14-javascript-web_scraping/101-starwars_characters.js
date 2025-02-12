#!/usr/bin/node
// Script that prints all characters of a Star Wars movie.

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (charErr, charResponse, charBody) => {
        if (charErr) {
          console.log(charErr);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});

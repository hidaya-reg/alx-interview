#!/usr/bin/node

const request = require('request');

function fetchCharacter(arr, index) {
  if (index >= arr.length) return;

  request(arr[index], (err, res, body) => {
    if (!err && res.statusCode === 200) {
      console.log(JSON.parse(body).name);
      fetchCharacter(arr, index + 1);
    } else {
      console.error('Error fetching character:', err);
    }
  });
}

request(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, res, body) => {
    if (!err && res.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      fetchCharacter(characters, 0); // Start fetching characters
    } else {
      console.error('Error fetching movie:', err);
    }
  }
);

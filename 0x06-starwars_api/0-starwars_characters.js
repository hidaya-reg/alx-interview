#!/usr/bin/node

const request = require('request');

function fetchCharacters(characters, index) {
  if (index >= characters.length) return;
  request(characters[index], (err, res, body) => {
    if (!err && res.statusCode === 200) {
      console.log(JSON.parse(body).name);
      fetchCharacters(characters, index + 1);
    }
  });
}

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    fetchCharacters(characters, 0);
  }
});

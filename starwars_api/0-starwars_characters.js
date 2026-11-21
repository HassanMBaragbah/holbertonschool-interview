#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(filmUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error('Characters not found');
    return;
  }

  const data = JSON.parse(body);
  if (!Array.isArray(data.characters)) {
    console.error('Characters not found');
    return;
  }

  printCharacters(data.characters, 0);
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (err, res, body) => {
    if (err) {
      console.error(err);
      return;
    }

    if (res.statusCode === 200) {
      console.log(JSON.parse(body).name);
    }

    printCharacters(characters, index + 1);
  });
}

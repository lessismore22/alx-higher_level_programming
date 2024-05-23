#!/usr/bin/node
/**
 * this module gets the title of a star wars movie
 *
*/
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, response, body) => {
	if (err) {
		console.log(err);
	} else {
	  const data = JSON.parse(body).title;
	  console.log(`${title}`);
	}
      });

#!/usr/bin/node
// a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});

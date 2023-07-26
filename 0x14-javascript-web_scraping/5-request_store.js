#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const url = process.argv[2];
const filename = process.argv[3];
const fs = require('fs');
const request = require('request');
request(url).pipe(fs.createWriteStream(filename));

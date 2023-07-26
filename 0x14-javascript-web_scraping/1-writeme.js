#!/usr/bin/node
// A  script that reads and prints the content of a file.

const filename = process.argv[2];
const text = process.argv[3];
const fs = require('fs');
fs.writeFile(filename, text, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});

'use strict';

// Imports
const worldCup = require('./file-list').worldCup;
const worldCupYears = require('./file-list').years;

// External Modules
let fs = require('fs');
let glob = require('glob');

for (let i = 0; i < worldCupYears.length; i++) {

  glob('./data/world-cup/' + worldCupYears[i] + '--*/cup.txt', function (er, files) {
    if (files.length > 0) {
      console.log(files)
      fs.readFile(files[0], 'utf8', function (err,data) {
        if (err) {
          return console.log(err);
        }
        //console.log(data);
        var arr = data.split("\n");
        console.log(arr);
      });
    }
  });
}

console.log(worldCup['1930']);

#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const stars = JSON.parse(body).characters;
  exactOrder(stars, 0);
});
const exactOrder = (stars, a) => {
  if (a === stars.length) return;
  request(stars[a], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(stars, a + 1);
  });
};

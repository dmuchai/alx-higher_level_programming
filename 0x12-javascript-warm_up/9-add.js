#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const argument1 = parseInt(process.argv[2]);
const argument2 = parseInt(process.argv[3]);

console.log(add(argument1, argument2));

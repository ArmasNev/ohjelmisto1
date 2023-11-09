'use strict';
const target = document.querySelector('#target');

const name = prompt("Enter your name:");

const rand = Math.floor(Math.random() * 4) + 1;

console.log(name, rand )

let clas;
switch (rand) {
  case 1:
    clas = 'Griffindor'
    break;
  case 2:
    clas = 'Griffindor'
    break;
  case 3:
    clas = 'Griffindor'
    break;
  case 4:
    clas = 'Griffindor'
    break;
}

target.innerHTML = `${name}, you are ${clas}.`
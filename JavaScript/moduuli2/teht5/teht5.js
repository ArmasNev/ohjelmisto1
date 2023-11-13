'use strict';

const numbersList = [];
let number = +prompt(`Enter number.`);
let numberInList = false;

while (!numbersList.includes(number)) {
  numbersList.push(number);
  number = +prompt(`Enter number.`);
}

const target = document.querySelector("#target");

numbersList.sort();

console.log(`Number ${number} was already given!`);
for (let num of numbersList) {
  console.log(num);
}
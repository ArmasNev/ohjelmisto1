'use strict';

const diceNumbers = +prompt(`How many dice do you want to roll?`);
const sumOfDice = +prompt(`Which sum do you want to get?`);

function roll() {
  return Math.floor(Math.random() * 6) + 1;
}

let chance = 0;

for (let j = 0; j < 100000; j++) {
  let sum = 0;
  for (let i = 0; i < diceNumbers; i++) {
    sum += roll();
  }
  if (sum === sumOfDice) {
    chance += 1;
  }
}

let probability = ((chance / 100000) * 100).toFixed(2);
document.querySelector('#target').innerHTML = `Probability to get sum ${sumOfDice} with ${diceNumbers} dice is ${probability}%.`;

`use strict`;

const diceNumbers = +prompt(`How many dices you want to roll?`);
function roll() {
  const result = Math.floor(Math.random()*6)+1;
  return result;
}
let sum = 0;
let diceResults = '';
const element = document.querySelector('#target');

for (let i = 0; i < diceNumbers; i++) {
  let dice = roll();
  diceResults += `Dice rolled. Result: ${dice}.<br>`;
  sum += dice;
}

element.innerHTML = `${diceResults} Sum of dices rolls is ${sum}.`;

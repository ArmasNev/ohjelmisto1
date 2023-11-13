'use strict';

function roll() {
  const result = Math.floor(Math.random()*6)+1;
  return result;
}

const diceNumbers = [];

let dice = 0;

while (dice != 6) {
  dice = roll();
  diceNumbers.push(dice);
}

const target = document.querySelector("#target");

let HTMLcode = `<ul>`;
for (let num of diceNumbers) {
  HTMLcode += `<li>${num}</li>`
}
HTMLcode += `</ul>`;
target.innerHTML +=HTMLcode






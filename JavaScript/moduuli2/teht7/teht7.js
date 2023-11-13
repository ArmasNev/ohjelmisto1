`use strict`;

const diceNumbers = [];

const diceSides = +prompt("Enter number of sides:");

let dice = 0;

function roll() {
  const result = Math.floor(Math.random()*diceSides)+1;
  return result;
}

while (dice != diceSides) {
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
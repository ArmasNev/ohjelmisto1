'use strict';

const numbers = [];

let number = +prompt("Give number. Enter 0 to stop.");

while (number !== 0) {
  numbers.push(number);
  number = +prompt("Give number. Enter 0 to stop.");
}

numbers.sort((a,b) => a-b);
numbers.reverse();
for (let num of numbers) {
  console.log(num);
}

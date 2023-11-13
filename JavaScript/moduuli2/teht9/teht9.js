`use strict`;
const someNumbers = [];
const evenNumbers = [];
let number = 0;

function random() {
  const result = Math.floor(Math.random()*100)+1;
  return result;
}

for (let i = 0; i < 10; i++) {
  number = random();
  someNumbers.push(number);
}
for ( let j = 0; j < someNumbers.length; j++) {
  if (someNumbers[j] % 2 === 0){
    evenNumbers.push(someNumbers[j]);
  }
}

console.log(someNumbers);
console.log(evenNumbers);
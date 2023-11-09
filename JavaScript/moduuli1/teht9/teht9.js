'use strict';

const number = +prompt('Enter integer:');

let prime = 'is';

if(number === 1) {
  prime = 'is not';
}
for (let i = 2; i < number; i++){
  const result = number % i;
  if (result === 0) {
    prime = 'is not';
    break;
  }
}

document.querySelector('#target').innerHTML = `${number} ${prime} prime number`
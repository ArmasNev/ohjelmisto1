'use strict';

const num1 = +prompt('Enter 1 number');
const num2 = +prompt('Enter 2 number');
const num3 = +prompt('Enter 3 number');

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

const element = document.querySelector('#target');

element.innerHTML = `Sum is ${sum}, product is ${product}, average is ${average}.`;

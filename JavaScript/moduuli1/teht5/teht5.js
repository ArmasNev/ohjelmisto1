//Write a program that asks the user to enter a year and notifies the user whether the input year
// is a leap year. A year is a leap year if it is divisible by four.
// However, years divisible by 100 are leap years only if they are also divisible by 400.
// Print the result on the HTML document. (3p)

'use strict';

const year = +prompt('Enter a year number:');

let leapYear=false;

if (Number.isInteger(year/400)) {
  leapYear = true;
}
else if (Number.isInteger(year/100)){
  leapYear = false;
}
else if (Number.isInteger(year/4)){
  leapYear = true;
}
const element = document.querySelector('#target');
if (leapYear === true) {
  element.innerHTML = `${year} is leap year.`;
}
else if (leapYear === false) {
  element.innerHTML = `${year} is not a leap year.`;
}










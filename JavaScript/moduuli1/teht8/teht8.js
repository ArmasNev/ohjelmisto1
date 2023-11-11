`use strict`;
const startYear = +prompt("Enter start year:");
const endYear = +prompt("Enter end year:");
let leapYears = ``;
for (let year = startYear; year <= endYear; year++) {
  if (year % 400 == 0  || (year % 4 == 0  && year % 100 != 0)) {
    leapYears += `<li>${year}</li>`
  }
}
const element = document.querySelector('#target');
element.innerHTML = leapYears;

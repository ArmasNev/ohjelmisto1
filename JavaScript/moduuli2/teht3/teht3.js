'use strict'

const dogNames = [];

for (let i = 0; i < 6; i ++) {
  let dogName = prompt(`Enter dog name.`)
  dogNames.push(dogName)
}
dogNames.sort();
dogNames.reverse();
const target = document.querySelector("#target");

let HTMLcode = `<ul>`;
for (let name of dogNames) {
  HTMLcode += `<li>${name}</li>`
}
HTMLcode += `</ul>`;
target.innerHTML +=HTMLcode
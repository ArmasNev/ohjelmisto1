'use strict'

const names = [];

let number = +prompt("How many participants?");

for ( let i=0;i<number; i++) {
  let name = prompt("Enter name of participant:")
  names.push(name);
}

names.sort();

const target=document.querySelector("#target");

target.createElement = `Names in alphabetical order.`
const ol = document.createElement('ol');
for (let start of names) {
  const li = document.createElement('li');
  li.appendChild(document.createTextNode(start));
  ol.appendChild(li);
}

target.appendChild(ol);

`use strict`;
const target = document.querySelector("#target");
const l1 = document.createElement('li');
const f = document.createTextNode('First item');
l1.appendChild(f);
const l2 = document.createElement('li');
const s = document.createTextNode('Second item');
l2.appendChild(s);
const l3 = document.createElement('li');
const t = document.createTextNode('Third item');
l3.appendChild(t);
target.appendChild(l1);
target.appendChild(l2);
target.appendChild(l3);
lI = document.getElementById('target').getElementsByTagName('li')[1];
lI.classList.add('my-item')
'use strict';

const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
const target = document.querySelector("#target");
for (const student of students) {
  const opt = document.createElement('option');
  opt.value = student.id;
  opt.appendChild(document.createTextNode(student.name));
  target.appendChild(opt);
}
`use strict`

const names = [`Johnny`, `DeeDee`, `Joey`, `Marky`];
let concatNames = ``;
for (let i = 0; i < names.length; i++) {
  concatNames += names[i];
}
document.querySelector('#target').innerHTML = concatNames;
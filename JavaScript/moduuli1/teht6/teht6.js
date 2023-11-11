`use strict`;

sqRootQuestion = confirm(`Should I calculate the square root?`);
if (sqRootQuestion) {
  sqRootInput = +prompt(`Enter number:`);
  if (sqRootInput > 0) {
    sqRootResult = `Square root to number ${sqRootInput} is ${Math.sqrt(sqRootInput)}.`;
  }
  else if(sqRootInput < 0) {
    sqRootResult = `The square root of a negative number is not defined.`;
  }
  else {
    sqRootResult = `Incorrect input.`;
  }
}
else {
  sqRootResult = `The square root is not calculated.`
}
const element = document.querySelector('#target');
element.innerHTML = sqRootResult;


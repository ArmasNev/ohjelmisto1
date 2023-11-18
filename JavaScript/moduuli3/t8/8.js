`use strict`;

const button = document.querySelector(`#start`);
const result = document.querySelector(`#result`);
const num1 = document.querySelector(`#num1`);
const num2 = document.querySelector(`#num2`);
const operation = document.querySelector(`#operation`);

function Calculation(n1, n2) {

    if (operation.value === `add`) {
            return n1 + n2;
    }
    else if (operation.value === `sub`) {
            return n1 - n2;
    }
    else if (operation.value === `multi`) {
            return n1 * n2;
    }
    else if (operation.value === `div`) {
            return n1 / n2;
    }

}

button.addEventListener('click', function (evt) {
    result.textContent = `Result: ${Calculation(Number(num1.value), Number(num2.value))}`;
});
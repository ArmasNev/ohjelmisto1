`use strict`;

const button = document.querySelector('#start');
const result = document.querySelector('#result');
const calculation = document.querySelector('#calculation');
function Calculation(n1, n2, calcText) {

    if (calcText.includes('+')) {
            return n1 + n2;
    }
    else if (calcText.includes('-')) {
            return n1 - n2;
    }
    else if (calcText.includes('*')) {
            return n1 * n2;
    }
    else if (calcText.includes('/')) {
            return n1 / n2;
    }
}

button.addEventListener('click', function () {
    const calcText = calculation.value;
    const numbers = calcText.split(/[\/*+-]/);
    result.textContent = `Result: ${Calculation(Number(numbers[0]), Number(numbers[1]), calcText)}`;
});



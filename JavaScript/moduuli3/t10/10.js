'use strict';
const form = document.querySelector('form');
const firstName = document.querySelector('input[name=firstname]');
const lastName = document.querySelector('input[name=lastname]');
const target = document.querySelector(`#target`);

// When the form is submitted...
form.addEventListener('submit', function(evt) {
    evt.preventDefault();
    target.innerText = `Your name is ${firstName.value} ${lastName.value}`;
});
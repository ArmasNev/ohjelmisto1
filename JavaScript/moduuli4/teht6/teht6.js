'use strict';

const form = document.querySelector('form');
const results = document.querySelector('#result');

form.addEventListener('submit', async function(event) {
    event.preventDefault();
    const input_value = document.querySelector('#query').value;
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${input_value}`);
    const jokes = await response.json();
    results.innerHTML = '';
    for (const joke of jokes.result) {
        const article = document.createElement('article');
        const par = document.createElement('p');
        par.innerText = joke.value;
        article.appendChild(par);
        results.appendChild(article);
    }
});
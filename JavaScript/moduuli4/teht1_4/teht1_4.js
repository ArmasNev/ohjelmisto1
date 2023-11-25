'use strict';

const form = document.querySelector('form');
const results = document.querySelector('#result')

form.addEventListener('submit', async function(event) {
    event.preventDefault();
    const search_word = document.querySelector('#query').value;
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${search_word}`);
    const shows = await response.json();
    results.innerHTML = '';
    for(const tvshow of shows){


        const article = document.createElement('article');
        const header = document.createElement('h2');
        header.innerText = tvshow.show.name;
        const img = document.createElement('img');
        //let pic = '';
        //if(show.show.image) {
            //pic = show.show.image.medium;
        //}
        //else {
            //pic = 'https://placekitten.com/210/295';
        //}
        //img.src = pic;
        img.src = tvshow.show.image ? tvshow.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
        img.alt = tvshow.show.name;
        const link = document.createElement('a');
        link.href = tvshow.show.url;
        link.target = "_blank";
        link.innerText = tvshow.show.name;
        const summary = document.createElement('div');
        summary.innerHTML = tvshow.show.summary;


        article.appendChild(header);
        article.appendChild(img);
        article.appendChild(link);
        article.appendChild(summary);
        results.appendChild(article);
    }
});


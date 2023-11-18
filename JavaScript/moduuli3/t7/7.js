`use strict`;

const text = document.querySelector(`#trigger`);
const image = document.querySelector(`#target`);

text.addEventListener(`mouseover`, function() {
    image.src = `img/picB.jpg`;
})

text.addEventListener(`mouseout`, function() {
    image.src = `img/picA.jpg`;
})
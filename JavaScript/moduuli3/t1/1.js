`use strict`;
const HTML = `<li>First item</li>
<li>Second item</li>
<li>Third item</li>`;
const target = document.querySelector("#target");
target.classList.toggle('my-list')
target.innerHTML = HTML;
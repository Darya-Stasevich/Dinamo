const links = document.querySelectorAll('.aside__list-item');
const general = document.getElementById('#general__information');
const numbers = document.getElementById('#history__numbers');
const start = document.getElementById('#content__start');
const reconstruction = document.getElementById('#reconstruction');
const ceremony = document.getElementById('#ceremony');
const voice = document.getElementById('#voice');
const facts = document.getElementById('#facts');
const articles = document.getElementById('#articles');



let array = []
array.push(general,numbers,start,reconstruction,ceremony,voice,facts,articles)


for (let i = 0; i < links.length; i++){
    links[i].addEventListener('click', () => {
    scrollBy(0, (array[i].getBoundingClientRect().top - 100))
        // console.log(windowScrollTop)
        // console.log(array[i].getBoundingClientRect().top)
        // console.log(windowScrollTop + array[i].getBoundingClientRect().top)
    })
}


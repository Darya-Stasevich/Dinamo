let header = document.querySelector('.header');

window.addEventListener('scroll', function scrollHeader() {
    let scrolled = window.scrollY;

    if (scrolled == 0 && window.innerWidth > 992) {
        header.style = 'display: block;';
    }
    if (scrolled > 1 && window.innerWidth > 992) {
        header.style = 'position : fixed';
    }
});

let headerBurger = document.querySelector('.header__burger');
let headerMenu = document.querySelector('.menu__container');

headerBurger.addEventListener('click', showMenu);

function showMenu() {
    headerBurger.classList.toggle('active');
    headerMenu.classList.toggle('active');
    if (headerBurger.classList.contains('active')) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }

};
let menuExtraBlock = document.querySelector('.menu-extra__block');
let menuMobileContainer = document.querySelector('.menu-mobile__container');

function get_category(url) {
    fetch(url)
<<<<<<< HEAD
        .then(response=>response.json())
        .then(categories=>{
            for (let i of categories){
                menuExtraBlock.innerHTML+=`<a href="{% url 'show_services_by_category' ${i.slug} %}" class="menu-extra__link">${i.title}</a>`
                console.log(i.slug)
            }
        })
}
get_category('http://127.0.0.1:8000/api_dinamo/category_services/');
=======
        .then(response => response.json())
        .then(categories => {
            for (let i of categories) {
                menuExtraBlock.innerHTML += `<a href="/services/${i.slug}" class="menu-extra__link">${i.title}</a>`
            }
        })
}

get_category('https://hicnh32749.pythonanywhere.com/api_dinamo/category_services/');

>>>>>>> 51ddcdc0d5d2d9d7ac6aea0358859e505720ca2b
function get_category_mobile(url) {
    fetch(url)
        .then(resp => resp.json())
        .then(categories => {
            for (let i = 0; i < categories.length; i = i + 2) {
                menuMobileContainer.innerHTML += `<div><a href="/services/${categories[i].slug}" class="menu-extra__link">${categories[i].title}</a><a href="/services/${categories[i + 1].slug}">${categories[i + 1].title}</a></div>`
            }
        })
}
<<<<<<< HEAD
get_category_mobile('http://127.0.0.1:8000/api_dinamo/category_services/')
=======

get_category_mobile('https://hicnh32749.pythonanywhere.com/api_dinamo/category_services/')
>>>>>>> 51ddcdc0d5d2d9d7ac6aea0358859e505720ca2b


window.onload = function () {

    document.addEventListener('click', headerActions)

    function headerActions(e) {
        const targetElement = e.target;

        let menuServices = document.querySelector('.list__item.services');
        let menuMedia = document.querySelector('.list__item.media');

        let menuExtraContainer = document.querySelector('.menu-extra__container');
        menuExtraContainer.addEventListener('click', e => {
            e.stopPropagation()
        });

        let menuExtraMedia = document.querySelector('.menu-extra__media');
        menuExtraMedia.addEventListener('click', e => {
            e.stopPropagation()
        });

        if (targetElement.id == 'services') {
            menuServices.classList.toggle('hover');
        } else {
            menuServices.classList.remove('hover');
        }
        if (targetElement.id == 'media') {
            menuMedia.classList.toggle('hover');
        } else {
            menuMedia.classList.remove('hover');
        }

    }
}

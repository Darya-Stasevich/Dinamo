"use strict"

let position = 0;
let slidersToShow = 3;
if(window.innerWidth > 1200){
    slidersToShow = 4;
} else if(window.innerWidth > 992 && window.innerWidth < 1200){
    slidersToShow = 3;
} else if(window.innerWidth > 768 && window.innerWidth < 992){
    slidersToShow = 2;
} else{
    slidersToShow = 1;
}
const slidersToScroll = 1;
const container = document.querySelector('.news__container');
const track = document.querySelector('.news');
const btnPrev = document.querySelector('.news__left');
const btnNext = document.querySelector('.news__right');
const items = document.querySelectorAll('.news__item');
const itemWidth = container.clientWidth / slidersToShow;
const movePosition = slidersToScroll * itemWidth;
function get_news(url) {
    fetch(url)
        .then(response => response.json())
        .then(cards => {
            for(let i of cards){
                track.innerHTML += `<div class="news__item" style="min-width: ${itemWidth}px;background: url(${i.cover_image}) center/cover no-repeat">
                    <div class="item__background">
                        <div class="item__block">
                            <p class="item__title">${i.title}</p>
                            <p class="item__subtitle">${i.brief_description}</p>
                            <a href="#" class="item__link">Читать полностью</a>
                        </div>
                    </div>
                </div>`
            }
            if (window.innerWidth >= 992){
                if (cards.length <= 4){
                    btnNext.style.display = 'none';
                    btnPrev.style.display = 'none';
                }else {
                    btnPrev.style.display = 'block';
                    btnNext.style.display = 'block';
                }
            }
            else {
                btnPrev.style.display = 'block';
                btnNext.style.display = 'block';
            }
        })
}
get_news('https://hicnh32749.pythonanywhere.com/api_dinamo/news/')

items.forEach((item) => {
    item.style.minWidth = `${itemWidth}px`;
});

btnNext.addEventListener('click', () => {
    const itemsCounter = document.querySelectorAll('.news__item')
    const itemsLeft = itemsCounter.length - (Math.abs(position) + slidersToShow * itemWidth) / itemWidth;
    if(itemsLeft === 0){

    }else {
        position -= itemsLeft >= slidersToScroll ? movePosition : (itemsLeft * itemWidth) / itemsLeft;
    }
    setPosition();
    checkBtns();
});

btnPrev.addEventListener('click', () => {
    const itemsLeft = Math.abs(position) / itemWidth;
    position += itemsLeft >= slidersToScroll ? movePosition : itemsLeft * itemWidth;

    setPosition();
    checkBtns();
});

const setPosition = () => {

    track.style.transform = `translateX(${position}px)`;
};

const checkBtns = () => {
    const itemsCounter = document.querySelectorAll('.news__item')
    btnPrev.disabled = position === 0;
    // btnNext.disabled = position <= - (itemsCounter.length - slidersToShow) * itemWidth;
    btnNext.disabled = position <= -(itemsCounter.length * itemWidth);
    if(btnNext.disabled === true){
        position = -(itemsCounter.length * itemWidth);
    }
};


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
const itemCount = items.length;
const itemWidth = container.clientWidth / slidersToShow;
const movePosition = slidersToScroll * itemWidth;


items.forEach((item) => {
    item.style.minWidth = `${itemWidth}px`;
});

btnNext.addEventListener('click', () => {
    const itemsLeft = itemCount - (Math.abs(position) + slidersToShow * itemWidth) / itemWidth;

    position -= itemsLeft >= slidersToScroll ? movePosition : itemsLeft * itemWidth;

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
    btnPrev.disabled = position === 0;
    btnNext.disabled = position <= - (itemCount - slidersToShow) * itemWidth;
};
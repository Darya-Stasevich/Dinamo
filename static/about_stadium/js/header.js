let header = document.querySelector('.header');

window.addEventListener('scroll', function scrollHeader() {
	let scrolled = window.scrollY;

    if (scrolled == 0 && window.innerWidth > 992){
        header.style = 'display: block;';
    }
    if( scrolled > 1 && window.innerWidth > 992){
        header.style = 'position : fixed';
    }
});

let headerBurger = document.querySelector('.header__burger');
let headerMenu = document.querySelector('.menu__container');

    headerBurger.addEventListener('click', showMenu);

    function showMenu(){
        headerBurger.classList.toggle('active');
        headerMenu.classList.toggle('active');
    };

window.onload = function (){
    let headerList = document.querySelector('.header__list');
        headerList.addEventListener('click', headerActions);

    function headerActions (e){
        const targetElement = e.target;

        let menuServices = document.querySelector('.list__item.services');
        let menuMedia = document.querySelector('.list__item.media');

        if (window.innerWidth > 992){
            if (targetElement.id == 'services'){
                menuServices.classList.toggle('hover');
                menuMedia.classList.remove('hover');
            }
            if (targetElement.id == 'media'){
                menuMedia.classList.toggle('hover');
                menuServices.classList.remove('hover');
            }
        }
        if (window.innerWidth < 992){
            if (targetElement.id == 'services'){
                menuServices.classList.toggle('hover');
                menuMedia.classList.remove('hover');
            }
            if (targetElement.id == 'media'){
                menuMedia.classList.toggle('hover');
                menuServices.classList.remove('hover');
            }
        }
    }
}

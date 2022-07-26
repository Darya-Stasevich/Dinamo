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
        if (headerBurger.classList.contains('active')){
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = 'auto';
        }

    };


window.onload = function (){

    document.addEventListener('click', headerActions)

    function headerActions (e){
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

            if(targetElement.id == 'services'){
                menuServices.classList.toggle('hover');
            }
            else{
                menuServices.classList.remove('hover');
            }
            if(targetElement.id == 'media'){
                menuMedia.classList.toggle('hover');
            } else{
                menuMedia.classList.remove('hover');
            }

    }
}

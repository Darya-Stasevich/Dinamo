let media = document.querySelector('.media__wrap');
let show = document.querySelector('.show');
let showBlock = document.querySelector('.show-media');
let mediaItem = document.querySelectorAll('.media__item');
let showMediaImg = document.querySelector('.show-media__img')
const photoButton = document.querySelector('.media__button-foto');
const videoButton = document.querySelector('.media__button-video');

mediaItem.forEach(item => item.addEventListener('click', (e)=> {
    event.preventDefault()
    let a = item.querySelector('img').getAttribute('src');
    showMediaImg.querySelector('img').setAttribute('src',a);

}))
    media.addEventListener('click', showMedia)
    function showMedia(e){
        let target = e.target.tagName;
        if(target === 'IMG'){
                show.style.display = 'block';
                showBlock.style.display = 'block'
        }
    }

let mediaCross = document.querySelector('.show-media__cross');
    mediaCross.addEventListener('click', closeMedia);
    function closeMedia(){
        showBlock.style.display = 'none';
        show.style.display = 'none';
    }
    photoButton.classList.add('media__button-active');
    photoButton.addEventListener('click', ()=> {
        photoButton.classList.add('media__button-active');
        if(videoButton.classList.contains('media__button-active')){
            videoButton.classList.remove('media__button-active');
        }
    })
    videoButton.addEventListener('click', ()=> {
        videoButton.classList.add('media__button-active')
        if(photoButton.classList.contains('media__button-active')){
            photoButton.classList.remove('media__button-active');
        }
    })
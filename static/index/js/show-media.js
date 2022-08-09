let media = document.querySelector('.media__wrap');
let show = document.querySelector('.show');
let showBlock = document.querySelector('.show-media');
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
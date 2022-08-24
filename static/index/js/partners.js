const partnersWrapper = document.querySelector('.partners__wrapper')



function fn(url) {
    fetch(url)
        .then(response => response.json())
        .then(res => {
            for (let i of res){
                partnersWrapper.innerHTML += ` <div class="partners__item">
                                                    <img src="${i.image}" alt="">
                                                </div>`
            }
        })
}
fn('https://hicnh32749.pythonanywhere.com/api_dinamo/partners/')

const serviceCommercial = document.querySelector('.service__commercial');
const serviceWrapper = document.querySelector('.service__commercial-wrapper')
const carouselWrapper = document.querySelector('.carousel__page')
const arrowRight = document.querySelector('.carousel__right');
const arrowLeft = document.querySelector('.carousel__left');
const serviceWrap = document.querySelector('.service__wrapper');
const serviceComerc = document.querySelector('.service__commercial-main');


let commercialWidth = serviceCommercial.clientWidth;
function get_service(url) {
    fetch(url)
        .then(response => response.json())
        .then(service => {
            let idItem = 0;
            let setItem = false;
            // for (let k = 0; k < service.length; k++){
            //     if (service[k].is_primary_service){
            //         idItem = service[k];
            //         setItem = true
            //         break
            //     }
            // }
            service.forEach((item, index) => {
                if (service[index].is_primary_service){
                    idItem = service[index];
                    setItem = true
                }
            })
            if(setItem){
                serviceComerc.innerHTML += `
                        <div class="service__rent" style="background: url(${idItem.image}) center/cover no-repeat">
                            <a href="#" class="rent__background">
                                <p class="rent__text">${idItem.title}</p>
                                <div class="rent__link"></div>
                            </a>
                            <a href="/services" class="service__link">
                                Смотреть все услуги
                            </a>
                        </div>`
            }else if (idItem === 0) {
                serviceComerc.innerHTML += `
                        <div class="service__rent" style="background: url(${service[0].image}) center/cover no-repeat">
                            <a href="#" class="rent__background">
                                <p class="rent__text">${service[0].title}</p>
                                <div class="rent__link"></div>
                            </a>
                            <a href="/services" class="service__link">
                                Смотреть все услуги
                            </a>
                        </div>`
            }
            // -----------------------
            for (let i = 0; i < service.length; i = i + 4){
                serviceWrapper.innerHTML += `<div class="commercial__container">
                                                <a href="#" class="commercial__block">
                                                    <div class="commercial__background" style="background: url(${service[i].image}) center/cover no-repeat">
                                                        <p class="commercial__text">${service[i].title}</p>
                                                    </div>
                                                </a>
                                                <a href="#" class="commercial__block">
                                                    <div class="commercial__background" style="background: url(${service[i + 1]?service[i + 1].image:''}) center/cover no-repeat">
                                                        <p class="commercial__text">${service[i + 1] ? service[i + 1].title:''}</p>
                                                    </div>
                                                </a>
                                                <a href="#" class="commercial__block">
                                                    <div class="commercial__background" style="background: url(${service[i + 1]?service[i + 2].image:''}) center/cover no-repeat">
                                                        <p class="commercial__text">${service[i + 2] ? service[i + 2].title:''}</p>
                                                    </div>
                                                </a>
                                                <a href="#" class="commercial__block">
                                                    <div class="commercial__background" style="background: url(${service[i + 1]?service[i + 3].image:''}) center/cover no-repeat">
                                                        <p class="commercial__text">${service[i + 3] ? service[i + 3].title:''}</p>
                                                    </div>
                                                </a>
                                            </div>`
            }
            let containers = document.querySelectorAll('.commercial__container');
            for (let j of containers){
                carouselWrapper.innerHTML += `<div class="page"></div>`
            }
            let cardWidth = document.querySelector('.commercial__container').clientWidth;
            if (window.innerWidth > 1260){
                cardWidth = 600;
                containers.forEach(item => {
                    item.style.minWidth = `${cardWidth}px`;
                })
            }
            if (window.innerWidth <= 768){
                cardWidth = commercialWidth - 16;
                containers.forEach(item => {
                    item.style.minWidth = `${cardWidth}px`;
                })
            }
            const pages = document.querySelectorAll('.page');
            let pos = 0;
            let count = 0;
            function setPos(){
                serviceWrapper.style.transform = `translateX(${pos}px)`
            }
            function setPage(){
                if (count == 0){
                    pages[0].classList.add('page__color')
                }else {
                    if (count == pages.length){

                    }else {
                        pages[count - 1].classList.remove('page__color')
                    }
                    pages[count].classList.add('page__color')
                }
            }
            setPage()
            arrowRight.addEventListener('click', () => {
                if (pos == -(containers.length * cardWidth) + cardWidth - (30 * containers.length) + 30){
                    pos = -(containers.length * cardWidth) + cardWidth - (30 * containers.length) + 30;
                } else {
                    pos -= containers.length * cardWidth / containers.length + 30;
                }
                if (count == pages.length - 1){
                } else {
                    count += 1;
                }
                setPos()
                setPage()
            })
            arrowLeft.addEventListener('click', () => {
                if(pos == 0){
                    pos = 0;
                }else {
                    pos += containers.length * cardWidth / containers.length + 30;
                }
                if (count == 0){
                } else {
                    pages[count].classList.remove('page__color')
                    count -= 1;
                }
                setPos()
                setPage()
            })
        })
}
get_service('https://hicnh32749.pythonanywhere.com/api_dinamo/services/')





const vacancyWrapper = document.querySelector('.vacancy__block-wrapper');

function showVacancy() {
    const titleWrapper = document.querySelectorAll('.vacancy__block-title-wrapper');
    const vacancyBlock = document.querySelectorAll('.vacancy__block');
    vacancyBlock.forEach(item => {
        item.addEventListener('click', (e) => {
            let currentTarget = e.currentTarget;
            let target = e.target;
            titleWrapper.forEach(items => {
                if (target == items){
                    currentTarget.classList.toggle('show-vacancy__block')
                    let respondTitle = document.getElementById('respond__title');
                    respondTitle.innerHTML = `${items.innerText}`;
                }
            })
        })
    })
}



function showRespond() {
    document.querySelector('.container__background').style.display = 'block';
    document.querySelector('main').classList.toggle('showrespond');
    const containerRespond = document.querySelector('.container__respond')
        containerRespond.style.display = 'block';
    if (containerRespond.style.display === 'block'){
        document.body.style.overflow = 'hidden';
        containerRespond.style.overflow = 'auto';
        containerRespond.style.height = '80%';
    }else {
        document.body.style.overflow = 'auto';
    }
}
let respondClose = document.querySelector('.respond__cross');
    respondClose.addEventListener('click', () => {
        document.querySelector('.container__background').style.display = 'none';
        document.querySelector('main').classList.remove('showrespond');
        document.querySelector('.container__respond').style.display = 'none';
        document.body.style.overflow = 'auto';
    })
let buttonSend = document.querySelector('.form__button');
buttonSend.addEventListener('click', sendRespond);
let sendButton = document.querySelector('.send__button');
    sendButton.addEventListener('click', () => {
        const containerSend = document.querySelector('.container__send');
            containerSend.style.display = 'none';
        document.querySelector('main').classList.remove('showrespond')
        document.querySelector('.container__background').style.display = 'none';
    })
function sendRespond() {
    document.querySelector('.container__respond').style.display = 'none';
    const containerSend = document.querySelector('.container__send');
        containerSend.style.display = 'flex';
    if (containerSend.style.display === 'flex'){
        document.body.style.overflow = 'auto';
    }

}

function get_vacancy(url) {
    fetch(url)
        .then(response => response.json())
        .then(vacancy => {
            for (let i = 0; i < vacancy.length; i++) {
                vacancyWrapper.innerHTML += `<div class="vacancy__block">
                                                    <div class="vacancy__block-title-wrapper">
                                                    ${vacancy[i].title_of_vacancy}
                                                    </div>
                                                    <div class="vacancy__block-about">
                                                        <ul class="about-list__title">
                                                            <li>ЗП: <span>${vacancy[i].salary}</span></li>
                                                            <li>Опыт работы: <span>${vacancy[i].experience}</span></li>
                                                            <li>Занятость: ${vacancy[i].employment}</li>
                                                        </ul>
                                                        <p class="list__title">
                                                            ${vacancy[i].vacancyrequirements_set[0].title}
                                                        </p>
                                                        <ul class="about__list">
                                                            ${vacancy[i].vacancyrequirements_set[0].list_of_requirements}
                                                        </ul>
                                                        ${vacancy[i].vacancyrequirements_set[1] ? `<p class="list__title">${vacancy[i].vacancyrequirements_set[1].title}</p>`:''}
                                                        ${vacancy[i].vacancyrequirements_set[1] ? `<ul class="about__list">${vacancy[i].vacancyrequirements_set[1].list_of_requirements}</ul>`:''}
                                                        ${vacancy[i].vacancyrequirements_set[2] ? `<p class="list__title">${vacancy[i].vacancyrequirements_set[2].title}</p>`:''}
                                                        ${vacancy[i].vacancyrequirements_set[2] ? `<ul class="about__list">${vacancy[i].vacancyrequirements_set[2].list_of_requirements}</ul>`:''}
                                                        ${vacancy[i].vacancyrequirements_set[3] ? `<p class="list__title">${vacancy[i].vacancyrequirements_set[3].title}</p>`:''}
                                                        ${vacancy[i].vacancyrequirements_set[3] ? `<ul class="about__list">${vacancy[i].vacancyrequirements_set[3].list_of_requirements}</ul>`:''}
                                                        ${vacancy[i].vacancyrequirements_set[4] ? `<p class="list__title">${vacancy[i].vacancyrequirements_set[4].title}</p>`:''}
                                                        ${vacancy[i].vacancyrequirements_set[4] ? `<ul class="about__list">${vacancy[i].vacancyrequirements_set[4].list_of_requirements}</ul>`:''}
                                                        ${vacancy[i].vacancyrequirements_set[5] ? `<p class="list__title">${vacancy[i].vacancyrequirements_set[5].title}</p>`:''}
                                                        ${vacancy[i].vacancyrequirements_set[5] ? `<ul class='about__list'>${vacancy[i].vacancyrequirements_set[5].list_of_requirements}</ul>`:''}
                                                        <button class="list__button">Откликнуться</button>
                                                    </div>
                                                </div>`
                let buttonRespond = document.querySelectorAll('.list__button');
                buttonRespond.forEach(item => {
                    item.addEventListener('click', showRespond);
                })
                showVacancy()
            }
        })
}

get_vacancy('https://hicnh32749.pythonanywhere.com/api_dinamo/vacancies/')
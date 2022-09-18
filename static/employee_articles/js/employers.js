const employersWrapper = document.querySelector('.main__employers-card-wrapper')
const input = document.getElementById('numberPage');
const searchInput = document.getElementById('searchInput')
const pages = document.querySelector('.total__pages');
const searchButton = document.querySelector('.main__search-button')
let count = 0;
let numberPage = 0;
input.setAttribute('value', 1);
input.oninput = () => {
    input.value = input.value.replace(/[^0-9]/g, '')
}
function get__employers(url) {
    fetch(url)
        .then(request => request.json())
        .then(employers => {
            let sortArrayEmployer
            if (searchInput.value == ''){
                sortArrayEmployer = employers;
                console.log(sortArrayEmployer)
            }
            searchInput.oninput = () => {
                searchInput.value = searchInput.value.replace(/[^a-zа-яё\s]/gi, '');
                if(searchInput.value != '') {
                    sortArrayEmployer = employers.filter((employerObj) => {
                        if (employerObj.name_employee == searchInput.value){
                            return employerObj.name_employee;
                        }
                    })
                    console.log(sortArrayEmployer)
                }else {
                    sortArrayEmployer = employers;
                    let searchCardsTwo = document.querySelectorAll('.main__employers-card')
                    searchCardsTwo.forEach(item => {
                        item.remove()
                    })
                    for (let i = 0; i < sortArrayEmployer.length; i++){
                        let date = new Date(sortArrayEmployer[i].created)
                        employersWrapper.innerHTML += `<a href="#" class="main__employers-card">
                                                <div class="main__employers-card-image">
                                                    <img src="${sortArrayEmployer[i].cover_image}" alt="">
                                                    <div class="main__employers-card-hover">
                                                        <img src="/static/employee_articles/img/icons/rent_link.svg" alt="">
                                                    </div>
                                                </div>
                                                <div class="main__employers-card-text-wrapper">
                                                    <div class="main__employers-card-date">
                                                        ${date.toLocaleString('default', {year: 'numeric', month: 'long', day:'numeric' })}
                                                    </div>
                                                    <div class="main__employers-card-text">
                                                        <span class="main__employers-card-name">${sortArrayEmployer[i].name_employee}.</span> ${sortArrayEmployer[i].title}
                                                    </div>
                                                </div>
                                            </a>`
                        count++
                    }
                }
            }

            searchButton.addEventListener('click', () => {
                let searchCards = document.querySelectorAll('.main__employers-card')
                searchCards.forEach(item => {
                    item.remove()
                })
                for (let i = 0; i < sortArrayEmployer.length; i++){
                    let date = new Date(sortArrayEmployer[i].created)
                    employersWrapper.innerHTML += `<a href="#" class="main__employers-card">
                                                <div class="main__employers-card-image">
                                                    <img src="${sortArrayEmployer[i].cover_image}" alt="">
                                                    <div class="main__employers-card-hover">
                                                        <img src="/static/employee_articles/img/icons/rent_link.svg" alt="">
                                                    </div>
                                                </div>
                                                <div class="main__employers-card-text-wrapper">
                                                    <div class="main__employers-card-date">
                                                        ${date.toLocaleString('default', {year: 'numeric', month: 'long', day:'numeric' })}
                                                    </div>
                                                    <div class="main__employers-card-text">
                                                        <span class="main__employers-card-name">${sortArrayEmployer[i].name_employee}.</span> ${sortArrayEmployer[i].title}
                                                    </div>
                                                </div>
                                            </a>`
                    count++
                }
            })
            for (let i = 0; i < sortArrayEmployer.length; i++){
                let date = new Date(sortArrayEmployer[i].created)
                employersWrapper.innerHTML += `<a href="#" class="main__employers-card">
                                                <div class="main__employers-card-image">
                                                    <img src="${sortArrayEmployer[i].cover_image}" alt="">
                                                    <div class="main__employers-card-hover">
                                                        <img src="/static/employee_articles/img/icons/rent_link.svg" alt="">
                                                    </div>
                                                </div>
                                                <div class="main__employers-card-text-wrapper">
                                                    <div class="main__employers-card-date">
                                                        ${date.toLocaleString('default', {year: 'numeric', month: 'long', day:'numeric' })}
                                                    </div>
                                                    <div class="main__employers-card-text">
                                                        <span class="main__employers-card-name">${sortArrayEmployer[i].name_employee}.</span> ${sortArrayEmployer[i].title}
                                                    </div>
                                                </div>
                                            </a>`
                count++
            }
            for (let j = 0; j < employers.length; j += 16){
                numberPage++
            }
            pages.innerHTML += numberPage;
        })
}
get__employers('https://hicnh32749.pythonanywhere.com/api_dinamo/employee_article/');
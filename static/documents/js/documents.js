const blockWrapper = document.querySelector('.documents__block-wrapper');
let a = '/static/documents/img/icons/downloadIcon.svg'

function get_documents(url) {
    fetch(url)
        .then(request => request.json())
        .then(documents => {
            console.log(documents)
            for (let i of documents){
                blockWrapper.innerHTML += `<div class="documents__block">
                                            <div class="documents__block-title">
                                                ${i.title}
                                            </div>
                                            <a href='${i.file}' class="documents__block-download-wrapper">
                                                <img src="${a}" alt="">
                                                <span>Скачать</span>
                                            </a>
                                        </div>`
            }
        })
}
get_documents('https://hicnh32749.pythonanywhere.com/api_dinamo/documents/')
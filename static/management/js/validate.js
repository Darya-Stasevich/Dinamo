const  form = document.querySelector('.footer__form');
const input = document.querySelector('.form-block__input');

form.onsubmit = function (){
    let inputVal = input.value;
    let val = input.value == '';
    if(inputVal == '' || val.length == 0){
        input.style.borderColor = 'red';
        return false
    }
}
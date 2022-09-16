const  form = document.querySelector('.footer__form');
const input_email = document.querySelector('.form-block__input');

form.onsubmit = function (){
    let inputVal = input_email.value;
    let val = input_email.value == '';
    if(inputVal == '' || val.length == 0){
        input_email.style.borderColor = 'red';
        return false
    }
}
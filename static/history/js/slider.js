const sliderPoints = document.querySelectorAll('.slider__points');
const text = document.querySelectorAll('.main__content-reconstruction-about');
const nextArrow = document.querySelectorAll('.slider-wrapper-right-arrow');
const prevArrow = document.querySelectorAll('.slider-wrapper-left-arrow');
let counter = 0;
if(counter == 0){
    sliderPoints[0].classList.add('isActive');
    text[0].classList.add('selected');
    prevArrow.forEach(item => {
        item.style.background = 'url("/static/history/img/icons/arrow_left_button.svg") no-repeat center, #C2A98A'
    })
}
nextArrow.forEach(arrow => {
    arrow.addEventListener('click', () => {
        if (counter == sliderPoints.length - 1){
            counter = sliderPoints.length - 1;
        }else {
            counter++
            console.log(counter)
            sliderPoints[counter].classList.add('isActive')
            sliderPoints[counter - 1].classList.remove('isActive')
            text[counter].classList.add('selected');
            text[counter - 1].classList.remove('selected');
        }
        if (counter == sliderPoints.length - 1){
            arrow.style.background = 'url("/static/history/img/icons/arrow_right_button.svg") no-repeat center, #C2A98A'
        }
        if (counter != 0){
            prevArrow.forEach(item => {
                item.style.background = 'url("/static/history/img/icons/arrow_left_button.svg") no-repeat center, linear-gradient(180deg, #C89555 0%, #9E6D2F 100%)';
            })
        }
    })
})
prevArrow.forEach(arrow => {
    arrow.addEventListener('click', () => {

        if (counter == 0) {
            counter = 0;
        }else {
            counter--
            console.log(counter)
            sliderPoints[counter].classList.add('isActive');
            sliderPoints[counter + 1].classList.remove('isActive');
            text[counter].classList.add('selected');
            text[counter + 1].classList.remove('selected');
        }
        if (counter != sliderPoints.length - 1){
            nextArrow.forEach(item => {
                item.style.background = 'url("/static/history/img/icons/arrow_right_button.svg") no-repeat center, linear-gradient(180deg, #C89555 0%, #9E6D2F 100%)'
            })
        }
        if (counter == 0){
            prevArrow.forEach(item => {
                item.style.background = 'url("/static/history/img/icons/arrow_left_button.svg") no-repeat center, #C2A98A'
            })
        }
    })
})

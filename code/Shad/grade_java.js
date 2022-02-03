console.log('pool')
let input = document.getElementById('input')
let submit = document.getElementById('submit')
let result = document.querySelector('#result')
submit.addEventListener('click', grade)
function grade() {
    console.log(input.value)
    if (input.value > 90) {
        console.log('A')
        result.innerText = 'A'
    }
    else if (input.value > 80) {
        console.log(' B')
        result.innerText = 'B'
    }
    else if (input.value > 70) {
        console.log('C')
        result.innerText = 'C'
    }
    else if (input.value > 60) {
        console.log(' D')
        result.innerText = 'D'
    }
    else if (input.value < 60) {
        console.log('F')
        result.innerText = 'F'
    }
}
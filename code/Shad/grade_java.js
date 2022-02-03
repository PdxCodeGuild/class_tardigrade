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
    else if (input > 80) {
        console.log(' B')
        result.innerText = 'B'
    }
    else if (input > 70) {
        console.log('C')
        result.innerText = 'C'
    }
    else if (input > 60) {
        console.log(' D')
        result.innerText = 'D'
    }
    else if (input < 60) {
        console.log('F')
        result.innerText = 'F'
    }
}
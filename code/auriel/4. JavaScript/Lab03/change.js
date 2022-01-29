let user = parseFloat(prompt('Enter a dollar amount'))
let money = user / .01

let quarters 
let dimes
let nickels
let pennies

if (user <= 0) {
    alert('Error')
}
else {
    quarters = money % 25
}

alert(`${quarters}`)
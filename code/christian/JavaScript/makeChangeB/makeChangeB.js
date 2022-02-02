

let amountInput = document.querySelector('#amount-input')
let getChangeButton = document.querySelector('#get-change')
let output = document.querySelector('#output')

getChangeButton.addEventListener('click', function(){
    let userInput = amountInput.value * 100
    let quarters = userInput / 25 
    quarters = Math.floor(quarters)
    userInput = userInput % 25
    let dimes = userInput / 10
    dimes = Math.floor(dimes)
    userInput = userInput % 10
    let nickles = userInput / 5
    nickles = Math.floor(nickles)
    userInput = userInput % 5
    userInput = Math.floor(userInput)

    output.innerText = `${quarters} quarters,${dimes} dimes,${nickles} nickles,${userInput} pennies`





})





// let cents = (parseInt(prompt('Enter a dollar amount: '))* 100)

// let quarters = cents / 25 
// quarters = Math.floor(quarters)
// cents = cents % 25
// let dimes = cents / 10
// dimes = Math.floor(dimes)
// cents = cents % 10
// let nickles = cents / 5
// nickles = Math.floor(nickles)
// cents = cents % 5
// cents = Math.floor(cents)

// alert(`${quarters} quarters,${dimes} dimes,${nickles} nickles,${cents} pennies`)
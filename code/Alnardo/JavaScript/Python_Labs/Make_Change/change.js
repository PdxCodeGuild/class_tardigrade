// alert('Welcome to the Change-Maker') //For Part A

const changeInput = document.querySelector('#change_input')

const numberButton = document.querySelector('#number_button')

const totalCoins = document.querySelector('#total_coins')

numberButton.addEventListener('click', function() {
    
    total_amount = +changeInput.value
    console.log(changeInput)
    console.log(total_amount)
    // total_amount = parseFloat(total_amount) //For Part A
    
    change = total_amount * 100
    
    quarters = Math.floor(change / 25)
    dimes = Math.floor(((change - (quarters * 25)) / 10)) 
    nickles = Math.floor(((change - (quarters * 25) - (dimes * 10)) / 5))
    pennies = Math.floor(((change - (quarters * 25) - (dimes * 10) - (nickles * 5) / 1)))
    
    // alert(`You have ${quarters} quarters, ${dimes} dimes, ${nickles} nickles, and ${pennies} pennies.`) //For Part A

    totalCoins.innerText = `You have ${quarters} quarters, ${dimes} dimes, ${nickles} nickles, and ${pennies} pennies.`
})

// Part A Complete \\

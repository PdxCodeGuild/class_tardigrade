let user = parseFloat(prompt('Enter a dollar amount'))
let money = user / .01

let quarters; 
let dimes;
let nickels;
let pennies;
let remainder;

if (user <= 0) {
    alert('Error')
}
else {
    quarters = Math.floor(money / 25)

    remainder = money % 25
    dimes = Math.floor(remainder / 10)

    remainder = money % 25 % 10
    nickels = Math.floor(remainder / 5)

    remainder = money % 25 % 10 % 5
    pennies = Math.floor(remainder / 1)
}

alert(`You have ${quarters} Quarters, ${dimes} Dimes, ${nickels} Nickels, ${pennies} Pennies`)
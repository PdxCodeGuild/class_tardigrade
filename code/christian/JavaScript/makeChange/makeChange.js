
let cents = (Number(prompt('Enter a dollar amount: '))* 100)

let quarters = cents / 25 
quarters = Math.floor(quarters)
cents = cents % 25
let dimes = cents / 10
dimes = Math.floor(dimes)
cents = cents % 10
let nickles = cents / 5
nickles = Math.floor(nickles)
cents = cents % 5
cents = Math.floor(cents)

alert(`${quarters} quarters,${dimes} dimes,${nickles} nickles,${cents} pennies`)
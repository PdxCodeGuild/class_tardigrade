let inputChange= parseFloat(prompt("What amount would you like to convert to change? (i.e. 125.51)"))

inputChange= inputChange*100
const quarters= Math.floor(inputChange/25)
const quarterRemainder= inputChange % 25
const dimes= Math.floor(quarterRemainder/10)
const dimeRemainder= quarterRemainder % 10
const nickels= Math.floor(dimeRemainder/5)
const nickelRemainder= dimeRemainder % 5
const pennies= Math.floor(nickelRemainder/1)
const pennyRemainder= nickelRemainder % 1

alert(`${quarters} quarters, ${dimes} dimes, ${nickels} nickels, ${pennies} pennies`)

// console.log(`${quarters} quarters`)
// console.log(`${quarterRemainder} remainder`)
// console.log(`${dimes} dimes`)
// console.log(`${dimeRemainder} remainder`)
// console.log(`${nickels} nickels`)
// console.log(`${nickelRemainder} remainder`)
// console.log(`${pennies} pennies`)
// console.log(`${pennyRemainder} remainder`)


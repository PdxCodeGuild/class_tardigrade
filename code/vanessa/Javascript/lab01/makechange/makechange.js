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
alert(inputChange)
console.log("numberofquarters")
console.log(quarters)
console.log("remainder")
console.log(quarterRemainder)
console.log("numberofdimes")
console.log(dimes)
console.log("remainder")
console.log(dimeRemainder)
console.log("numberofnickels")
console.log(nickels)
console.log("remainder")
console.log(nickelRemainder)
console.log("numberofpennies")
console.log(pennies)
console.log("remainder")
console.log(pennyRemainder)


// for 1.98 (198) should have 7 quarters(1.75), 2 dimes (.20=1.95), 0 nickels, three pennies (.03=1.98).....need to fix after quarters/carryover remainder of quarters, etc.//
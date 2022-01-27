let inputChange= parseFloat(prompt("What amount would you like to convert to change? (i.e. 125.51)"))

inputChange= inputChange*100
const quarters= Math.floor(inputChange/25)
const quarterRemainder= inputChange % 25
const dimes= Math.floor(inputChange/10)
const dimeRemainder= inputChange % 10
const nickels= Math.floor(inputChange/5)
const nickelRemainder= inputChange % 5
const pennies= Math.floor(inputChange/1)
const pennyRemainder= inputChange % 1
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


/*every_cent = dollar_amount * 100

quarters = every_cent//25
print(f"{quarters} quarters")
quarters_remainder = every_cent % 25

dimes = quarters_remainder//10
print (f"{dimes} dimes")
dimes_remainder = quarters_remainder % 10


nickels = dimes_remainder//5
print (f'{nickels} nickels')
nickels_remainder = dimes_remainder%5

pennies = nickels_remainder//1
print (f'{pennies} pennies')
pennies_remainder = nickels_remainder%5*/
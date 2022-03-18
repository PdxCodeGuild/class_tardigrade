//JavaScript Lab 2
//Make change
//Author: Travis Jackson


// coin constant values
let coinAmountArray = {

quarter: 0,
dime: 0,
nickel: 0,
penny: 0
};

window.alert("Find change!")

let changeAmount = window.prompt("Enter dollar amount: ","")


let totalRemaining = changeAmount * 100


//quarters
let quarterCalc = Math.floor(totalRemaining / 25)

totalRemaining = totalRemaining - (quarterCalc * 25)

coinAmountArray.quarter = quarterCalc

//dimes

let dimeCalc = Math.floor(totalRemaining / 10)

totalRemaining = totalRemaining - (dimeCalc * 10)

coinAmountArray.dime = dimeCalc

//nickels

let nickelCalc = Math.floor(totalRemaining / 5)

totalRemaining = totalRemaining - (nickelCalc * 5)

coinAmountArray.nickel = nickelCalc

//pennies

let pennyCalc = Math.floor(totalRemaining / 1)

totalRemaining = totalRemaining - (pennyCalc * 1)

coinAmountArray.penny = pennyCalc

let output = ""

for (let key in coinAmountArray) {
    let value = coinAmountArray[key];
    let coinName = key;

    output = output.concat(` ${coinName}: ${value} `);

}

window.alert(output)

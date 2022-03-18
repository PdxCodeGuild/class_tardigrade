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


let listChange = document.getElementById("list-change");


function calcCoins(coinAmountArray, userEntry) {

    let totalRemaining = userEntry * 100


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


    return coinAmountArray
}



submitDollar.addEventListener('click', function (e) {
    e.preventDefault()

    listChange.innerText = ""

    

    //Get text entry
    let textEntry = document.querySelector("#text-entry");
    let userEntry = textEntry.value;


    //Calls calculate function. passes input
    calcCoins(coinAmountArray, userEntry);


    for (let key in coinAmountArray) {
        let value = coinAmountArray[key];
        let coinName = key;

        let liElement = document.createElement("li");


        output = (coinName + ": " + value);

        liElement.innerText = output;

        listChange.appendChild(liElement);

    }

});

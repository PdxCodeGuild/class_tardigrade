//JavaScript Lab 2
//Make change
//Author: Travis Jackson


// coin constant values
let coin_amount_dic = {

    quarter: 0,
    dime: 0,
    nickel: 0,
    penny: 0
};


let list_change = document.getElementById("list-change");


function calc_coins(coin_amount_dic, user_input) {

    let total_remaining = user_input * 100


    //quarters
    let quarter_calc = Math.floor(total_remaining / 25)

    total_remaining = total_remaining - (quarter_calc * 25)

    coin_amount_dic.quarter = quarter_calc

    //dimes

    let dime_calc = Math.floor(total_remaining / 10)

    total_remaining = total_remaining - (dime_calc * 10)

    coin_amount_dic.dime = dime_calc

    //nickels

    let nickel_calc = Math.floor(total_remaining / 5)

    total_remaining = total_remaining - (nickel_calc * 5)

    coin_amount_dic.nickel = nickel_calc

    //pennies

    let penny_calc = Math.floor(total_remaining / 1)

    total_remaining = total_remaining - (penny_calc * 1)

    coin_amount_dic.penny = penny_calc


    return coin_amount_dic
}



submit_dollar.addEventListener('click', function (e) {
    e.preventDefault()


    //Get text entry
    let text_entry = document.querySelector("#text-entry");
    let user_input = text_entry.value;


    //Calls calculate function. passes input
    calc_coins(coin_amount_dic, user_input);


    for (let key in coin_amount_dic) {
        let value = coin_amount_dic[key];
        let coin_name = key;

        let li_element = document.createElement("li");


        test = (coin_name + ": " + value);

        li_element.innerText = test;

        list_change.appendChild(li_element);

    }

});

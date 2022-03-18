const form = document.getElementById('form');

const amount = document.getElementById('amount');

const quarters = document.getElementById('quarters');

const dimes = document.getElementById('dimes');

const nickels = document.getElementById('nickels');

const pennies = document.getElementById('pennies');


form.onsubmit = function(event) {
    event.preventdefault();

    let user = parseFloat(amount.value);
    let money = user / .01;

    let qrt; 
    let dim;
    let nick;
    let penn;
    let remainder;

    if (user <= 0) {
        alert('Error')
    }
    else {
        qrt = Math.floor(money / 25)
    
        remainder = money % 25
        dim = Math.floor(remainder / 10)
    
        remainder = money % 25 % 10
        nick = Math.floor(remainder / 5)
    
        remainder = money % 25 % 10 % 5
        penn = Math.floor(remainder / 1)
    }

    
    quarters.innerHTML = qrt;
    dimes.innerHTML = dim;
    nickels.innerHTML = nick;
    pennies.innerHTML = penn;

}

document.getElementById('submit').onclick = function(){
    
    let user = parseFloat(amount.value);
    let money = user / .01;

    let qrt; 
    let dim;
    let nick;
    let penn;
    let remainder;

    if (user <= 0) {
        alert('Error')
    }
    else {
        qrt = Math.floor(money / 25)
    
        remainder = money % 25
        dim = Math.floor(remainder / 10)
    
        remainder = money % 25 % 10
        nick = Math.floor(remainder / 5)
    
        remainder = money % 25 % 10 % 5
        penn = Math.floor(remainder / 1)
    }

    
    quarters.innerText = qrt;
    dimes.innerText = dim;
    nickels.innerText = nick;
    pennies.innerText = penn;
}
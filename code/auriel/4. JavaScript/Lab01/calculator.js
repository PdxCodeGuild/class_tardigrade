const form = document.getElementById('form');

const number1 = document.getElementById('number1');

const number2 = document.getElementById('number2');

const results = document.getElementById('result');


form.onsubmit = function(event) {
    event.preventdefault();

    let newvalue = parseFloat(number1.value) + parseFloat(number2.value);
    results.innerHTML = newvalue;
}

document.getElementById('add').onclick = function(){

	let newvalue = parseFloat(number1.value) + parseFloat(number2.value);
    results.innerHTML = newvalue;
}

document.getElementById('subtract').onclick = function(){
	
	let newvalue = parseFloat(number1.value) - parseFloat(number2.value);
    results.innerHTML = newvalue;
}

document.getElementById('multiply').onclick = function(){
	
	let newvalue = parseFloat(number1.value) * parseFloat(number2.value);
    results.innerHTML = newvalue;
}

document.getElementById('divide').onclick = function(){
	
	let newvalue = parseFloat(number1.value) / parseFloat(number2.value);
    results.innerHTML = newvalue;
}
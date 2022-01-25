// for loops
let numbers = [3, 4, 1, 2, 5]
for (let i = 0; i < numbers.length; i++) {
	let number = numbers[i]
	console.log(number)
}


// functions
function add(x, y) {
	return x + y
}

alert(add(1, 2))

const subtract = function(x, y) {
	return x - y
}

alert(subtract(5, 3))

// arrow functions
const multiply = (x, y) => x * y
alert(multiply(7, 11))

function divide(options) {
	return options.firstNum / options.secondNum
}

let result = divide({
	firstNum: 55,
	secondNum: 5
})

alert(result)
// console.log(document.querySelector('#password'))

// gets the element with id="password"
const passwordElement = document.querySelector('#password')
// const passwordElement = document.getElementById('password')

// gets the element with id="password-button"
const passwordButton = document.querySelector('#password-button')

// gets the elemnt with id="number-input"
const numberInput = document.querySelector('#number-input')

// using element.onclick and an arrow function
// passwordButton.onclick = () => alert('you clicked me')

const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

// addEventListener is an HTML element method
// the first arguement is a string of the type of the event: i.e.: 'click', 'hover', 'input'
// the second argument is an anonymous function (a callback function), to be performed on the event
passwordButton.addEventListener('click', function () {
	// password will have chars concatenated to it, time to use let
	let password = ''

	// parseInt() function takes a string as argument and returns an integer
	// const passwordLength = parseInt(numberInput.value)

	// as a shorthand, putting + before a numeric string will give you a Number
	const passwordLength = +numberInput.value
	// console.log(typeof passwordLength) // Number

	// console.log(typeof numberInput.value) // String
	
	for (let i = 0; i < passwordLength; i++) {
		password += randomChoice(characters)
	}
	passwordElement.innerText = 'Your password is ' + password
	passwordElement.style.color = randomChoice(colors)
})

// characters is never reassigned, safe to use const

function randomChoice(arr) {
	return arr[Math.floor(Math.random() * arr.length)]
}


// alert(password) // for part A version
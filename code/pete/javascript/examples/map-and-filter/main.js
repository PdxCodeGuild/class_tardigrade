// // standard function declaration in JS
// function add (x, y) {
// 	return x + y
// }

// console.log(add(3, 4))

// // arrow function
// const multiply = (x, y) => x * y

// console.log(multiply(7, 11))


// // for loops
// const staff = ['pete', 'sheri', 'lisa', 'matt', 'ashton']

// // good old C style for loop
// for (let i=0; i<staff.length; i++) {
// 	console.log(staff[i])
// }

// // for (element of array) syntax
// for (employee of staff) { // more like for employee in staff: # in python
// 	console.log(employee) // you loop over the values
// }

// // for (index in array) syntax
// for (i in staff) { // the array is an object, you loop over the properties
// 	console.log(i)
// }

// // using an array method: forEach
// staff.forEach(employee => console.log(employee))
// staff.forEach((employee, index, arr) => { // forEach can take the element, index, and array
// 	arr[index] = employee.toUpperCase()
// })

// console.log(staff)

// array of objects, to be mapped & filtered

const teams = [
	{
		name: 'Rams',
		city: 'Los Angeles',
		conference: 'NFC',
		won: true
	},
	{
		name: '49ers',
		city: 'San Fransisco',
		conference: 'NFC',
		won: false
	},
	{
		name: 'Bengals',
		city: 'Cincinatti',
		conference: 'AFC',
		won: true
	},
	{
		name: 'Chiefs',
		city: 'Kansas City',
		conference: 'AFC',
		won: false
	}
]

// array.map takes in a callback function for each elemnt and returns a new array composed of the returns for that callback function
// The Los Angeles Rams play in the NFC.
const teamFacts = teams.map(team => `The ${team.city} ${team.name} play in the ${team.conference}`)
console.log(teamFacts)

// array.filter takes in a callback function for each element and returns a new array composed only of the elements whose callback functions return true
const winners = teams.filter(team => team.won === true)
console.log(winners)

const losers = teams.filter(team => team.won === false)
console.log(losers)

// chaining array methods
// The Los Angeles Rams won the AFC Championship Game.
const winnerFacts = teams.filter(team => team.won === true).map(team => `The ${team.city} ${team.name} won the ${team.conference} Championship Game 😤`)

console.log(winnerFacts)

const loserFacts = teams.filter(team => team.won === false)
												.map(team => {
													return `The ${team.city} ${team.name} lost the ${team.conference} Championship Game 😥`}
												)

console.log(loserFacts)
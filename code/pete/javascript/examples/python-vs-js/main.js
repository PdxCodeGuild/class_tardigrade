// arrays

const colors = ['red', 'green', 'blue']
// array.push(element)
colors.push('yellow')

// for (const color of colors) {
// 	console.log(color)
// }

// for (let i=0; i<colors.length; i++) {
// 	console.log(colors[i])
// }

function consoleLogColor (color) {
	console.log(color)
}

// colors.forEach(color => console.log(color))
// colors.forEach(consoleLogColor)

// objects

// console.log(typeof 1, typeof 'hello', typeof [1, 2, 3], typeof {a: 1})

const day = {
	month: 'January',
	weather: 'cold',
	'day-of-week': 'Friday',
	key: 'test'
}

const objKeys = ['month', 'weather', 'day-of-week']

console.log(day.month, day.weather, day['day-of-week'])

for (let i=0; i< objKeys.length; i++) {
	const key = objKeys[i]
	console.log(`The ${key} is ${day[key]}`)
}
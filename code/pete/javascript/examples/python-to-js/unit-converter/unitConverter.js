const unitToMeter = {
	ft: 0.3048,
	mi: 1609.34,
	m: 1,
	km: 1000
}

let unitFrom = prompt('enter a unit to convert to meters: ')
let units = prompt(`enter the number of ${unitFrom} to convert: `)

let result = units * unitToMeter[unitFrom]

console.log(unitToMeter.ft) // 0.3048
console.log(unitToMeter.m) // 1
console.log(unitToMeter.unitFrom) // undefined
console.log(unitToMeter[unitFrom]) // 1609.34 if unitFrom were 'mi'

alert(result)
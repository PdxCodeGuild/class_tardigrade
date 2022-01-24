let percentage = prompt('enter a percentage grade')

// console.log('hello')

// console.log(typeof percentage)

percentage = parseInt(percentage) // python equivalent percentage = int(percentage)


// console.log(typeof percentage)

let grade

if (percentage >= 90) {
	grade = 'A'
}
else if (percentage >= 80) {
	grade = 'B'
}
else if (percentage >= 70) {
	grade = 'C'
}
else if (percentage >= 60) {
	grade = 'D'
}
else {
	grade = 'F'
}

// alert('your grade is ' + grade)
alert(`your grade is: ${grade} ${percentage}`) // template literal, aka string interpolation, aka javascript f-string


let var1 = 1
let var2 = '2'
console.log(var1 + var2)

// let, const, var

// let number = 1
// alert(number)
// number += 1
// alert(number)

// const is a constant variable, cannot be redefined
// const number2 = 1
// alert(number2)
// number2 += 1 // cannot redefine constant variable
// alert(number2)

// const numbers = [1,2,3,4,5]
// numbers.push(6)
// numbers = [1, 2, 3, 4, 5, 6] // cannot redefine constant variable
// alert(numbers)
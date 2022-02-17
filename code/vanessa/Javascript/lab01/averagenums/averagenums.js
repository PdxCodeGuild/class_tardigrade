
let numbers=[]

let inputNumbers = prompt("please enter your number")
if (inputNumbers != "done"){
    numbers.push(parseInt(inputNumbers))
}
while (inputNumbers != "done") {
    inputNumbers = prompt("new number")
    if (inputNumbers != "done"){
        numbers.push(parseInt(inputNumbers))
    }
    // console.log(numbers)
}

let sum = 0
for (let i = 0; i < numbers.length; i++) {
    // let number = numbers[i]
    sum += numbers[i]
    console.log(sum)
}

// let average = sum/numbers.length
// console.log(average)
alert(sum/numbers.length)











// nums = [5, 0, 8, 3, 4, 1, 6]

// let selection = [4,7,3,2,8,1]

// function add (x,y) {
//         return x+y
// }
// alert(add(1,2))


// const subtract = function(x,y){
//         return x-y
// }
// alert(subtract(5,3))


// const multiply = (x,y) => x*y
// alert (multiply(7,11))

// function divide(options){
//     return options.firstNum/ options.secondNum
// }

// let result=divide({
//     firstNum: 55,
//     secondNum: 5
// })

// alert(result)


// let numbers = {
//     choice:1
// }
// let selection = 'number';
// numbers['selection']= 2
// console.log(numbers.choice)


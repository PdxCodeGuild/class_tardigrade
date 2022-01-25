nums = [5, 0, 8, 3, 4, 1, 6]

let numbers = [4,7,3,2,8,1]
for (let i = 0; i < numbers.length; i++) {
    let number = numbers [i]
    console.log(number)
}

function add (x,y) {
        return x+y
}
alert(add(1,2))


const subtract = function(x,y){
        return x-y
}

alert(subtract(5,3))
const multiply = (x,y) => x*y
alert (multipy(7,11))

function divide(options){
    return options.firstNum/ options.secondNum
}

let result=divide({
    firstNum: 55,
    secondNum: 5
})

alert(result)
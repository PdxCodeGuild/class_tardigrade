
let numbers = [5,0,8,3,4,1,6]

function sum(numbers){
    total_sum = 0
    for (x of numbers){
        total_sum += x
        console.log(x)


    }
    return total_sum
}
let result = sum(numbers)
let avg = result/numbers.length
alert(`The average is ${avg}`)


let numberlist = []

while (True){
    let choice = promt('Enter a number or "done" to finish: ')
    if (choice == 'done'){
        break
    }
    else{
        let choice = int(choice)
        numberlist.append(choice)
    }
}
let result = sum(numberlist)
let avg = result / numberlist.length

alert(`The average is ${avg}`)
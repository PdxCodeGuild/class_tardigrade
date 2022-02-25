let array = [];
let avg 

while (true) {
    let numbers = prompt('Eneter a number or done to quit ')

    if (numbers == 'done') {
        break
    }
    else {
        numbers = parseInt(numbers)
        array.push(numbers)
    }
}

avg = array.reduce((a, b) => a + b, 0) / array.length

alert(`${avg}`)

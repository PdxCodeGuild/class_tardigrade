


let numberInput = document.querySelector('#number-input')

const averageBtn = document.querySelector('#average-btn')

const addBtn = document.querySelector('#add-btn')

let numbers = []

addBtn.addEventListener('click', function (event) {
    event.preventDefault()
    let numberInputVal = numberInput.value
    numbers.push(numberInputVal)
    //need to add numbers together and divide by length






    console.log(numberInputVal)
    console.log(numbers)

})


averageBtn.addEventListener('click', function (event) {

    let sum = 0
    for (let i = 0; i < numbers.length; i++) {
        sum = sum + parseInt(numbers[i])
        console.log(sum)
    }

    let aveResult = sum / numbers.length
    // console.log(aveResult)
    let output = `The average is ${aveResult}`
    console.log(output)
    const average = document.querySelector('#average')
            // average.innerText='Hello World'
     average.innerText= output


})





// console.log(output)


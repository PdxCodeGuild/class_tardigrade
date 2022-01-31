// VERSION 1

// let nums = [5, 0, 8, 3, 4, 1, 6]

// let total = 0

// let i = 0

// while (i < nums.length) {
//     total += nums[i]
//     i++
// }

// let average = total / nums.length

// alert(average) // For Part A

// VERSION 2 Part A \\

// new_list = []

// let user_input = prompt("Please enter a number or type 'done'") // For Part A

// while (user_input != 'done') {
//     if (user_input == 'done') 
//         break
//     else
//         user_input = parseInt(user_input)
//         new_list.push(user_input)
        // user_input = prompt("Please enter a number or type 'done'") // For Part A
// }

// j = 0

// user_total = 0

// while (j < new_list.length) {
//     user_total += new_list[j]
//     j++
// }

// user_average = user_total / new_list.length

// alert(user_average) // For Part A

// Part A Complete \\

// Version 2 Part B \\


const user_input_num = document.querySelector('#user-input')
const finalCalculation = document.querySelector('#total-average')
const addButton = document.querySelector('#number-button')
const calculateButton = document.querySelector('#calculate-button')

let new_list = []

// addButton.onclick = () => alert('you clicked me') 

addButton.addEventListener('click', function(event) {
    event.preventDefault()
    // console.log(user_input_num.value)
    user_number = +user_input_num.value
    new_list.push(user_number)
    // console.log(new_list)
})


calculateButton.addEventListener('click', function(event) {
    event.preventDefault()
    sum = 0
    for (let i=0; i < new_list.length; i++) {
        sum += new_list[i]
    }

    calculated_mean = sum / new_list.length

    finalCalculation.innerText = `The average is ${calculated_mean}!`
})
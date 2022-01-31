// CREDIT CARD VALIDATION

const validationButton = document.querySelector('#validate-button')
const response = document.querySelector('#completed')

let creditNumbers = document.querySelector('#user-input')
let credit_nums = []
let new_credit_list = []

validationButton.addEventListener('click', function(event) {
    event.preventDefault()
    creditNumbers = creditNumbers.value
    for (let i=0; i < creditNumbers.length; i++) {
        num = creditNumbers[i]
        // console.log(num)
        credit_nums.push(num)
    }
    let check_num = credit_nums.pop()
    
    credit_nums.reverse()

    for (let i=0; i < credit_nums.length; i++) {
        let num = credit_nums[i]
        if (i % 2 == 0) {
            num = num * 2
            if (num > 9) {
                num = num - 9
                new_credit_list.push(num)
            }
            
            else {    
                new_credit_list.push(num)
            }
        }
        else {
            new_credit_list.push(num)
        }
    }
    
    let total = 0
    
    for (let j=0; j < new_credit_list.length; j++) {
        number = parseInt(new_credit_list[j])
        total += number
    }

    
    if (total % 10 == check_num) {
        response.innerText = 'This is a valid credit card!'
}
    else {
        response.innerText = 'This is not a valid credit card, you got scammed!'
    }
})



// Part B Complete \\
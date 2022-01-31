// CREDIT CARD VALIDATION

alert('Welcome to validating your credit card! Good luck!')

let credit_nums = []
let new_credit_list = []

while (credit_nums.length < 16) {
    user_input = prompt('Please enter the digits of your card one at a time')
    new_num = parseInt(user_input)
    credit_nums.push(new_num)
}

let check_num = credit_nums.pop()

alert(check_num)

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

// alert(new_credit_list)
let total = 0

for (let j=0; j < new_credit_list.length; j++) {
    let number = new_credit_list[j]
    total += number
}

alert(total)

if (total % 10 == check_num) {
    alert('This is a valid credit card!')
}
else {
    alert('This is not a valid credit card, you got scammed.')
}


// Part A Complete \\


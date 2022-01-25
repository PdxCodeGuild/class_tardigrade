// VERSION 1

let nums = [5, 0, 8, 3, 4, 1, 6]

let total = 0

let i = 0

while (i < nums.length) {
    total += nums[i]
    i++
}

let average = total / nums.length

alert(average)

// VERSION 2


new_list = []

let user_input = prompt("Please enter a number or type 'done'")

// new_list.push(user_input)

while (user_input != 'done') {
    if (user_input == 'done') 
        break
    else
        user_input = parseInt(user_input)
        new_list.push(user_input)
        user_input = prompt("Please enter a number or type 'done'")
}

j = 0

user_total = 0

while (j < new_list.length) {
    user_total += new_list[j]
    j++
}

user_average = user_total / new_list.length

alert(user_average)
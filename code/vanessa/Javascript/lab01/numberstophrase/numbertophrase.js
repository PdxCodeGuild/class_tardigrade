// hundreds_digit = Math.floor(inputNumber/100)
// hundreds_tenths = inputNumber % 100
// console.log(hundreds_digit)
// console.log(hundreds_tenths)
// hundreds[hundreds_digit],tens[hundreds_tenths]
// console.log(hundreds[hundreds_digit])
// console.log(tens[hundreds_tenths])
//objects (python=dictionaries)//
// let hundreds ={
//     0: " ",
//     1: "one-hundred",
//     2: "two-hundred",
//     3: "three-hundred",
//     4: "four-hundred",
//     5: "five-hundred",
//     6: "six-hundred",
//     7: "seven-hundred",
//     8: "eight-hundred",
//     9: "nine-hundred",
// }
// alert(inputNumber)
// console.log(tens[tens_digit])
// console.log(ones[ones_digit])


let inputNumber= parseInt(prompt("What number would you like to turn into a phrase? (whole numbers only 0-99)"))



let ones = {
    // 0: " ",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

let tens = {
    // 0: "and",
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
            }

let special = {
    0:  "zero",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",}




space=(' ')
tens_digit =  Math.floor((inputNumber%100)/10)
ones_digit = inputNumber%10
console.log(tens_digit)
console.log(ones_digit)




if (special.hasOwnProperty(inputNumber) === true){
    alert(special[inputNumber])
    
}
else {
    alert(tens[tens_digit]+space+ ones[ones_digit])

}


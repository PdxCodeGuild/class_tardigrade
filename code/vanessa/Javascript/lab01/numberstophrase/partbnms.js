let numberInput = document.querySelector('#number-input')

const phraseBtn = document.querySelector('#phrase-btn')


let ones = {
    0: " ",
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
    0: "and",
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
    0: "zero",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}


let hundreds = {
    0: " ",
    1: "one-hundred",
    2: "two-hundred",
    3: "three-hundred",
    4: "four-hundred",
    5: "five-hundred",
    6: "six-hundred",
    7: "seven-hundred",
    8: "eight-hundred",
    9: "nine-hundred",
}
//-----------------------------------------------------------------------//
phraseBtn.addEventListener('click', function (event) {


    let i = numberInput.value
    let x=parseInt(i)

    while (true) {
        hundreds_digit = parseInt(x/100)
        hundreds_tenths =parseInt(x % 100)
        tens_digit = parseInt((x % 100)/10)
        ones_digit = x % 10
        // console.log(`hundreds ${hundreds_digit}`)
        // console.log(`hundreds remainder ${hundreds_tenths}`)
        // console.log(`tens ${tens_digit}`)
        // console.log(`ones ${ones_digit}`)

        if (x in special) {
            // console.log(special[x])
            let output= `${special[x]}`
            const phrase= document.querySelector('#phrase')
            phrase.innerText= output
            break
        }
//---------------------------------------------------------------------------        

        if (!(x in special)) {
            
            let output= `${hundreds[hundreds_digit]} ${tens[tens_digit]} ${ones[ones_digit]}`
            const phrase= document.querySelector('#phrase')
            phrase.innerText= output
            break
        }
    }
})


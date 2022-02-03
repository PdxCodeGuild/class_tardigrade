
let dollarInput = document.querySelector('#dollar-input')

const changeBtn = document.querySelector('#change-btn')


changeBtn.addEventListener('click', function (event) {
    console.log(dollarInput.value)
    dollarInput.value= dollarInput.value*100
    const quarters= Math.floor(dollarInput.value/25)
    const quarterRemainder= dollarInput.value % 25
    const dimes= Math.floor(quarterRemainder/10)
    const dimeRemainder= quarterRemainder % 10
    const nickels= Math.floor(dimeRemainder/5)
    const nickelRemainder= dimeRemainder % 5
    const pennies= Math.floor(nickelRemainder/1)
    // const pennyRemainder= nickelRemainder % 1

    let Phrase= (`${quarters} quarters, ${dimes} dimes, ${nickels} nickels, ${pennies} pennies`)

    let output = `The number phrase is ${Phrase}`
    console.log(output)
    const changes = document.querySelector('#changes')
    changes.innerText = 'Hello World'
    changes.innerText = Phrase


})



const button = document.querySelector('#button')
let first_card = document.querySelector('#card1')
let second_card = document.querySelector('#card2')
let third_card = document.querySelector('#card3')
const advice = document.querySelector('#advice')

button.addEventListener('click', function () {

    let output1 = first_card.value
    let output2 = second_card.value
    let output3 = third_card.value

    const faceCards = {
        J: 10,
        K: 10,
        Q: 10,
        A: 1,
    }

    if (output1 in faceCards) {
        output1 = faceCards[output1]
        alert(output1, 'output1')
    }

    if (output2 in faceCards) {
        output2 = faceCards[output2]
        alert(output2, 'output2')
    }

    if (output3 in faceCards) {
        output3 = faceCards[output3]
        alert(output3, 'output3')
    }

    final = parseInt(output1) + parseInt(output2) + parseInt(output3)

    if (final < 17) {
        advice.innerText = `That's ${final} - I advise you to hit.`
    } else if (final >= 17 && final < 21) {
        advice.innerText = `That's ${final} - I advise you to stay.`
    } else if (final == 21) {
        advice.innerText = `That's ${final} - Blackjack!`
    } else {
        advice.innerText = `That's ${final} - Already busted!`
    }
})
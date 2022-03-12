let winNum = document.querySelector("#win-num")
let finalBalance = document.querySelector("#final-balance")
let roi = document.querySelector("#roi")
let startPick = document.getElementById("start-pick")

let balance = 0


function pick6() {

    let winningTicket = []
    for (let i = 0; i < 6; i++) {

        randomPick = Math.floor(Math.random() * 99)
        winningTicket.push(randomPick)
    }
    return winningTicket

};



function numMatches(winningTicket, ticket) {
    let ticketMatches = 0

    for (let j = 0; j < 6; j++) {

        if (winningTicket[j] == ticket[j]) {

            ticketMatches += 1
        }
    }

    return ticketMatches
};



startPick.addEventListener('click', function (e) {
    e.preventDefault();

    let ticket = []
    let balance = 0
    let earnings = 0
    let winningTicket = pick6()

    winNum.innerText = winningTicket;

    for (let i = 0; i < 1000000; i++) {

        balance -= 2
        ticket = pick6()

        matches = numMatches(winningTicket, ticket)

        if (matches == 0) {

        }
        else if (matches == 1) {
            balance += 4
            earnings += 0
        }
        else if (matches == 2) {
            balance += 7
            earnings += 7
        }
        else if (matches == 3) {
            balance += 100
            earnings += 100
        }
        else if (matches == 4) {
            balance += 50000
            earnings += 50000
        }
        else if (matches == 5) {
            balance += 1000000
            earnings += 1000000
        }
        else if (matches == 6) {
            balance += 25000000
            earnings += 25000000
        }

    }

   
    finalBalance.innerText = balance
    roi.innerText = ((earnings - 200000) / 200000) * 100

})








let win_num = document.querySelector("#win-num")
let final_balance = document.querySelector("#final-balance")
let roi = document.querySelector("#roi")
let start_pick = document.getElementById("start-pick")

let balance = 0


function pick6() {

    let winning_ticket = []
    for (let i = 0; i < 6; i++) {

        random_pick = Math.floor(Math.random() * 99)
        winning_ticket.push(random_pick)
    }
    return winning_ticket

};



function num_matches(winning_ticket, ticket) {
    let ticket_matches = 0

    for (let j = 0; j < 6; j++) {

        if (winning_ticket[j] == ticket[j]) {

            ticket_matches += 1
        }
    }

    return ticket_matches
};



start_pick.addEventListener('click', function (e) {
    e.preventDefault();

    let ticket = []
    let balance = 0
    let earnings = 0
    let winning_ticket = pick6()

    win_num.innerText = winning_ticket;

    for (let i = 0; i < 1000000; i++) {

        balance -= 2
        ticket = pick6()

        matches = num_matches(winning_ticket, ticket)

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

    console.log(earnings)
    final_balance.innerText = balance
    roi.innerText = ((earnings - 200000) / 200000) * 100

})








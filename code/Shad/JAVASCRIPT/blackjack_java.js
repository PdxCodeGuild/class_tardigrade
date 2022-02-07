let cards=  {'A':1,'2':2,'3':3,'4':4,'5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10,'K':10}
// let user2 = prompt ('What is your second card' )
// let user3 = prompt ('What is your third card' )

let firstInput = true
let secondInput = false

const button = document.querySelector('#button') // #button means the element with id="button"
console.log(button)
button.addEventListener('click', getAdvice)

const test = document.querySelector('#test')
//const test = document.getElementById('test')

const firstCardSelect = document.querySelector('#first-card')
const secondCardSelect = document.querySelector('#second-card')
const thirdCardSelect = document.querySelector('#third-card')
let results =document.getElementById('results')


function getAdvice(){
    
    let total = parseInt(firstCardSelect.value) + parseInt(secondCardSelect.value) + parseInt(thirdCardSelect.value )

    if (total > 21){
        alert ( 'you bust')
       results.innerText= 'you bust'
    }


    else if (total == 21){
        alert ( 'Blackjack')
        results.innerText= 'Blackjack'
        
    }
    else if (total <= 17){
        alert ( 'Hit?')
        results.innerText= 'Hit?'
        
    } 
        
        
    
}




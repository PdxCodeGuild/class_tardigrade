let toDoList=[]
let toDoButton = document.querySelector('#list')
let item = document.querySelector('#item')
let thingsList = document.querySelector('#things-list')
toDoButton.addEventListener('submit', function(event) {
			event.preventDefault()
            let itemValue = item.value
            toDoList.push(itemValue)
            const listLi = document.createElement('li')
            thingsList.appendChild(listLi)
            console.log(toDoList)
            listLi.innerText = itemValue

})
   

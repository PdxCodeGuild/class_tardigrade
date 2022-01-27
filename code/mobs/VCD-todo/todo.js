let toDoList=[]
let toDoButton = document.querySelector('#list')
let item = document.querySelector('#item')
toDoButton.addEventListener('submit', function(event) {
			event.preventDefault()
            let item = item.value
            toDoList.push(item)

})
    console.log(toDoList)

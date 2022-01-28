let toDoList = []
let toDoButton = document.querySelector('#list')
let item = document.querySelector('#item')
let thingsList = document.querySelector('#things-list')
toDoButton.addEventListener('submit', function (event) {
    event.preventDefault()
    let itemValue = item.value
    toDoList.push(itemValue)

    const listLi = document.createElement('li')
    thingsList.appendChild(listLi)

    const textSpan = document.createElement('span')
    textSpan.innerText = itemValue

    listLi.appendChild(textSpan)

    const complete = document.createElement('button')
    complete.innerText = "complete"
    listLi.appendChild(complete)

    const deleteButton = document.createElement('button')
    deleteButton.innerText = "delete"
    listLi.appendChild(deleteButton)

    console.log(toDoList)


    complete.addEventListener('click', function () {
        listLi.style.textDecoration = strike
    })

                
            })

            // deleteButton.addEventListener('click', function() {
            //     listLi.style.textDecoration = strike

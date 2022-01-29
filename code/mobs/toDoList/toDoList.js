const form = document.querySelector('form')

const input = document.querySelector('form > input')

const addButton = document.querySelector('#add-button')

const task = document.querySelector('#tasks')

const completedTask = document.querySelector('#completed')

form.addEventListener('submit', function(event) {
    event.preventDefault()

    let newTask = input.value
    let taskLi = document.createElement('li')
    let completeBtn = document.createElement("button")
    let deleteBtn = document.createElement("button")
    taskLi.innerText = newTask
    completeBtn.innerText = 'Complete'
    deleteBtn.innerText = 'Delete'
    task.appendChild(taskLi)
    taskLi.appendChild(completeBtn)
    taskLi.appendChild(deleteBtn)
    deleteBtn.addEventListener('click', function() {
        event.preventDefault()
        task.removeChild(taskLi)
    })
    
    completeBtn.onclick = function() {
        taskLi.style.textDecoration = "line-through";
        completedTask.appendChild(taskLi)
        deleteBtn.addEventListener('click', function() {
            event.preventDefault()
            completedTask.removeChild(taskLi)
        })
    }

})
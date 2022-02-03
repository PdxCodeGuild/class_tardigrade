let input = document.getElementById('input')
let submit = document.getElementById('submit')
let add = document.getElementById('add')
let deletion = document.getElementById('delete')
let complete = document.getElementById('complete')
let bullet =  document.getElementById('bullet')





add.addEventListener('click', add_)
function add_() {
    let node = document.createElement('li')
    let text = document.createTextNode(input.value)
    node.appendChild(text)
    node.setAttribute('id',input.value)

    bullet.appendChild(node)

        
    }



deletion.addEventListener('click',delete_)
function delete_() {  
    let deletion = document.getElementById(input.value)
    bullet.removeChild(deletion)
    
    console.log(deletion)
        
    }

complete.addEventListener('click', complete_)


function complete_() {

    let completed = document.getElementById(input.value)
    completed.classList.add('completed')

    
}





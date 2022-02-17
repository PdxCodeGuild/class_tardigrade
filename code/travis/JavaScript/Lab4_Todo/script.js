//text box entry
let add_entry = document.getElementById("add-entry");

//buttons
let add_button = document.getElementById("add-button");
let remove_button = document.getElementById("remove-button");
let completed_button = document.getElementById("completed-button");

//array
let todo_list_array = ["read", "go for a walk", "shopping", "schedule meeting"]

//
//starting entrys for testing
//
startingList(todo_list_array)

function startingList(todo_list_array){
for (let i=0; i < todo_list_array.length; ++i){
    var input_element = document.createElement("input")
    var label_element = document.createElement("label")



    let text_node = document.createTextNode(todo_list_array[i])


    label_element.appendChild(text_node)
    label_element.setAttribute("for", todo_list_array[i])
    label_element.innerText = todo_list_array[i]
    label_element.id = todo_list_array[i] + "label"

    input_element.appendChild(text_node)
    input_element.type = "radio"
    input_element.id = todo_list_array[i]
    input_element.name = "radio-items"



    document.getElementById("add-radio").append(label_element, input_element)
    //document.getElementById("add-radio").appendChild(label_element)
  //  document.getElementById("add-radio").appendChild(input_element)



}
}


//
//add to list button click
//
add_button.addEventListener("click", function(e){
    e.preventDefault();

   let entry_value = add_entry.value;
    todo_list_array.push(entry_value)
    var input_element_add = document.createElement("input")
    var label_element_add = document.createElement("label")

    let text_node = document.createTextNode(entry_value)



    label_element_add.appendChild(text_node)
    label_element_add.setAttribute("for", entry_value)
    label_element_add.innerText = entry_value
    label_element_add.id = entry_value + "label"


    input_element_add.appendChild(text_node)
    input_element_add.type = "radio"
    input_element_add.id = entry_value
    input_element_add.name = "radio-items"

    document.getElementById("add-radio").appendChild(label_element_add)
    document.getElementById("add-radio").appendChild(input_element_add)


});



//
// remove item from array, and radio button form
//
remove_button.addEventListener("click", function(e){

    e.preventDefault();

    for (j = 0; j < todo_list_array.length; j++) {

        let input_loop = document.getElementById(todo_list_array[j])
        let label_loop = document.getElementById(todo_list_array[j] + "label")


        if (input_loop.checked) {            

            document.getElementById("add-radio").removeChild(input_loop)
            document.getElementById("add-radio").removeChild(label_loop)
            todo_list_array.splice(j,1)
        }
      }
      
})



//
//complete item add to completed items list remove from array
//
completed_button.addEventListener("click", function(e){
    e.preventDefault();


    for (k = 0; k < todo_list_array.length; k++) {

        let input_loop = document.getElementById(todo_list_array[k])
        let label_loop = document.getElementById(todo_list_array[k] + "label")
        if (input_loop.checked) {            
            


            document.getElementById("add-radio").removeChild(input_loop)
            document.getElementById("add-radio").removeChild(label_loop)


        let li_element = document.createElement("li")

        let li_node = document.createTextNode(todo_list_array[k])
     
         li_element.appendChild(li_node)  


        document.getElementById("complete-list").appendChild(li_element)
        todo_list_array.splice(k,1)    
      
        }
      }


})





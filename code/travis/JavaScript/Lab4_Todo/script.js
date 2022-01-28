let todo_list_array = ["test1", "test2", "test3", "test4"]

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


document.getElementById("add-radio").appendChild(label_element)
document.getElementById("add-radio").appendChild(input_element)
}





//text box to add

add_entry = document.getElementById("add-entry");



//buttons
let add_button = document.getElementById("add-button");
let remove_button = document.getElementById("remove-button");
let completed_button = document.getElementById("completed-button");



//add to list button click
//
//
add_button.addEventListener("click", function(e){
    e.preventDefault();

    entry_value = add_entry.value;
    todo_list_array.push(entry_value)


    add_int = todo_list_array.length - 1
    console.log(add_int)
    let text_node = document.createTextNode(add_int)



    label_element.appendChild(text_node)
    label_element.setAttribute("for", todo_list_array[add_int])
    label_element.innerText = todo_list_array[add_int]
    label_element.id = todo_list_array[add_int] + "label"


    input_element.appendChild(text_node)
    input_element.type = "radio"
    input_element.id = todo_list_array[add_int]
    input_element.name = "radio-items"

    document.getElementById("add-radio").appendChild(label_element)
    document.getElementById("add-radio").appendChild(input_element)


});




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




completed_button.addEventListener("click", function(e){
    e.preventDefault();


    // change radio button text to linethrough
    console.log("test complete click");


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





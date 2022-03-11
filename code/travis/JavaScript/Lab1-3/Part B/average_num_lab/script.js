
let aveNumArray = []


let addButton = document.getElementById("add-button");
let numOutput = document.getElementById("num-list")
let averOut = document.getElementById("average")


addButton.onclick = function(e){
    e.preventDefault()
    let entryField = document.getElementById("entry-field").value;

    aveNumArray.push(parseInt(entryField))

    numOutput.innerText = aveNumArray    

}



let add = 0
let doneButton = document.getElementById("done-button");

doneButton.onclick = function(e){
    e.preventDefault();

    let arrayNum = aveNumArray.length;

 for(let k = 0; k < arrayNum; k++){

    add += aveNumArray.pop();

 }

 average = add / arrayNum

averOut.innerText = average
    aveNumArray = [];
    add = 0;
    arrayNum = 0;

}






// nums = [5, 0, 8, 3, 4, 1, 6]

// # loop over the elements
// for num in nums:
//     print(num)

// # loop over the indices
// for i in range(len(nums)):
//     print(nums[i])


console.log("for loop")
const nums = [5, 0, 8, 3, 4, 1, 6]

//let i = 0
for ( let i=0; i < nums.length; i++){
  //  console.log(nums[i])
}

console.log("while loop")
let j = 0
while ( j < nums.length){
  //  console.log(nums[j])
    j ++
}


console.log("for loop over elements")


for (num of nums){
//    console.log(num)
}


// Version 2

// Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.


// nums = []
// nums.append(5)
// print(nums)
// Below is an example input/output:

// > enter a number, or 'done': 5
// > enter a number, or 'done': 3
// > enter a number, or 'done': 4
// > enter a number, or 'done': done
// average: 4



let test_nums = [2,2,2,2]

let add_button = document.getElementById("add-button");

add_button.onclick = function(e){
    e.preventDefault()

    test_nums.push(2)

    alert(test_nums);
    

}



let add = 0
let done_button = document.getElementById("done-button");

done_button.onclick = function(e){
    e.preventDefault()
    array_num = test_nums.length

 for(let k = 0; k < array_num; k++){

    add += test_nums.pop()

 }

 average = add / array_num

    test_nums = []
    add = 0
    array_num = 0

}








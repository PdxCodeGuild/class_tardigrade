let ttl = document.getElementById("ttl");

let avg = document.getElementById("avg");

let number = document.getElementById("number");

let nums = [];



ttl.addEventListener("click", function (){

    console.log(number.value);

    nums.push(number.value);

    console.log(nums);

    const sum = nums.reduce((total, amount) => parseInt(total) + parseInt(amount));

    document.getElementById("total").innerHTML =  "Total: " + sum;

    avg.addEventListener("click", function(){
        z = sum / nums.length;
        document.getElementById("average").innerHTML = "Average: " + z;  
    
    });
});
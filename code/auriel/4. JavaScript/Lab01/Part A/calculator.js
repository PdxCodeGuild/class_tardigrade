let operation = prompt('What operation would you like to perform (+ * / -):');
let num1 = parseFloat(prompt('What is the first number: '));
let num2 = parseFloat(prompt('What is the second number: '));

let total;

if (operation == '+') {
    total = num1 + num2;
}
else if (operation == '-') {
    total = num1 - num2;
}
else if (operation == '*') {
    total = num1 * num2;
}
else if (operation == '/') {
    total = num1 / num2;
}

alert(`${num1} ${operation} ${num2} = ${total}`)
//num to phrase

number = int(prompt("Enter the number here: "))
var ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',];
var teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
var tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];

function numtophrase(s) {

}
if (number > 999)
    alert(f"{number} has too many digits, please enter a number below 1,000: ")
else if (number < 19)
    alert(ones[number])
else if (number < 99)
    alert(tens[tens_digit], ones[ones_digit])
else
    alert(ones[hundred_digit], " Hundred ", tens[tens_digit],ones[ones_digit])

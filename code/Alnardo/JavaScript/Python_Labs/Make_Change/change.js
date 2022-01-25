alert('Welcome to the Change-Maker')

total_amount = prompt('How much change do you have? Please enter in a 00.00 format')

total_amount = parseFloat(total_amount)

change = total_amount * 100

quarters = Math.floor(change / 25)
dimes = Math.floor(((change - (quarters * 25)) / 10)) 
nickles = Math.floor(((change - (quarters * 25) - (dimes * 10)) / 5))
pennies = Math.floor(((change - (quarters * 25) - (dimes * 10) - (nickles * 5) / 1)))

alert(`You have ${quarters} quarters, ${dimes} dimes, ${nickles} nickles, and ${pennies} pennies.`)
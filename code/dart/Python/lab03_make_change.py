while True:
    dollars = float(input("Enter a dollar amount so I can convert it to coins: "))
    pennies = int(dollars * 100)

    quarters = pennies // 25
    pennies = pennies % 25

    dimes = pennies // 10
    pennies = pennies % 10
    
    nickels = pennies // 5
    pennies = pennies % 5

    print(f"${dollars} equates to {quarters} quarters, {dimes} dimes, {nickels} nickels and {pennies} pennies.")

    answer = input("Do you want to go again? ")
    if answer == "no" or answer == "No" or answer == "nope" or answer == "Nope":    
        print("Okay, goodbye.")
        break
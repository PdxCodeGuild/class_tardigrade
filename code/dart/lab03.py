def coin_change(dollar_amount):
    if float(dollar_amount) <= 0:
        print("Error. You must enter a positive amount of money.")
    else:
        quarter = dollar_amount // 25
        dime = dollar_amount % 25 // 10
        nickel = dollar_amount % 25 % 10 // 5
        penny = dollar_amount % 5

coin_change(input("Enter a dollar amount: "))

class ATM:
    def __init__(self, balance=0, interest_rate=0.1, transactions=[]):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = transactions

    def check_balance(self): # return the account balance
        return self.balance

    def deposit(self, amount): # deposit a given amount into account
        self.balance += amount
        self.transactions.append(f"User deposited ${amount}.")
        return self.balance

    def check_withdrawal(self, amount): # return True if account has enough funds to withdraw given amount
        if amount <= self.balance:
            return True
        print(f"\n{amount} would overdraw the account.")
        return False

    def withdraw(self, amount): # withdraw given amount from account and return that amount
        self.balance -= amount
        self.transactions.append(f"User withrdew ${amount}.")
        return self.balance

    def calc_interest(self): # calculate and return interest gained on account
        interest = round((self.balance * self.interest_rate), 2)
        return interest

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)

def menu():
    print("\nPress [1] to Check Balance")
    print("\nPress [2] to Deposit Funds")
    print("\nPress [3] to Withdraw Funds")
    print("\nPress [4] to Check Interest")
    print("\nPress [5] to Check Transaction History")
    print("\nPress [6] to Exit")

atm = ATM()  # create an instance of our class
print("\033[1m" + "\n=======================\n" + "\033[0m")
print("\033[1m" + "  Welcome to the ATM!  " + "\033[0m")
print("\033[1m" + "\n=======================" + "\033[0m")
menu()
while True:
    command = int(input("\nEnter a command: "))
    if command == 1:
        balance = atm.check_balance()  # call the check_balance() method
        print(f"\nYour balance is ${balance}.")
        menu()
    elif command == 2:
        amount = float(input("\nHow much would you like to deposit: "))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f"\nDeposited ${amount}\n")
        menu()
    elif command == 3:
        amount = float(input("\nHow much would you like to withdraw: "))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f"\nWithdrew ${amount}.")
        else:
            print("\nInsufficient funds.\n")
        menu()
    elif command == 4:
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f"\nAccumulated ${amount} in interest.")
    # elif command == 5:
    #     print("\nAvailable commands:")
    #     print("balance  - get the current balance")
    #     print("deposit  - deposit money")
    #     print("withdraw - withdraw money")
    #     print("interest - accumulate interest")
    #     print("history  - transaction history")
    #     print("exit     - exit the program\n")
    elif command == 5:
        print("\n==========================\n")
        atm.print_transactions()
        print("\n==========================")
        menu()
    elif command == 6:
        print("\033[1m" + "\n==================================================\n")
        print("\033[1m" + "Goodbye! Thank You For Using PDX_Code_Guild Bank!")
        print("\033[1m" + "\n==================================================")
        break
    else:
        print("\nCommand not recognized.")
        menu()

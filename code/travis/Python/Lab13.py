"""
Lab 13: ATM
Author: Travis Jackson
Date:  12/6/21

"""


class ATM:


    def __init__(self, balance = 0, interest_rate = 0.001, transaction_list = []):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transaction_list = transaction_list



    def check_balance(self):
        """return the account balance"""

        return self.balance
      


    def deposit(self, amount):        
        """deposit a given amount into account"""

        self.balance += amount
        self.transaction_list.append(f"user deposited ${amount}")

    

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""

        if amount > self.balance:

            return False

        elif amount <= self.balance:

            return True



    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        
        self.balance -= amount
        self.transaction_list.append(f"user withdrew ${amount}")



    def calc_interest(self):        
        """calculate and return interest gained on account"""
    
        amount = self.interest_rate * self.balance
        return amount


    #version 2

    def print_transactions(self):
        

        for item in self.transaction_list:
            print(item)




atm = ATM()  # create an instance of our class
print('Welcome to the ATM')

while True:

    command = input('Enter a command: ')

    if command == 'balance':

        balance = atm.check_balance()  # call the check_balance() method

        print(f'Your balance is ${balance}')


    elif command == 'deposit':

        amount = float(input('How much would you like to deposit? '))

        atm.deposit(amount)  # call the deposit(amount) method



        print(f'Deposited ${amount}')


    elif command == 'withdraw':

        amount = float(input('How much would you like to withdraw? '))

        # call the check_withdrawal(amount) method


        if atm.check_withdrawal(amount):

            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')

            
        else:

            print('Insufficient funds')


    elif command == 'interest':

        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)

        print(f'Accumulated ${amount} in interest')


    elif command == 'help':


        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print("print - print your activity")
        print('exit     - exit the program')


    #Version 2
    elif command == "print":

        atm.print_transactions()


    elif command == 'exit':

        break

    else:

        print('Command not recognized')


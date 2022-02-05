from ast import Str


class ATM:

    def __init__(self, balance=0, interest_rate=0.1):
        self. balance = balance = 0
        self. interest = 0.1
        self.transactions = []
        
    def check_balance(self):
        return self.balance
        """return the account balance"""
    
    def deposit(self, amount):
        
        """deposit a given amount into account"""
        self.balance = amount + self.balance
        self.transactions.append(f'user deposit ${amount}')
        return self.balance


    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        if self.balance >= amount:
          return True
        else:
            False
            return False
        
    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance = self.balance - amount
        self.transactions.append(f'user withdrew ${amount}')

        return self.balance

    def calc_interest(self, ):

        """calculate and return interest gained on account"""

        
        return self.balance * .001
    
    def print_transactions(self):


        for i in self.transactions:
            print(i)
        return self.transactions 
def __str__(self):
    return self.balance 



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
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == "transactions":
        print(ATM.print_transactions)
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        # atm.calc_interest(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - transaction list')
        print('exit     - exit the program')
        
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
    


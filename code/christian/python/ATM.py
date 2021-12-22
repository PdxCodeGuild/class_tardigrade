class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate
        self.history = []

    def check_balance(self):
        return self.balance
            

        
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.history.append(f'You deposited {amount}')
        return self.balance
        

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

        
        

    def withdraw(self, amount):
        self.balance -= amount
        self.history.append(f'You withdrew {amount}')
        return self.balance


        
        """withdraw given amount from account and return that amount"""
        ...

    def calc_interest(self):
        interest= self.balance * self.interest_rate * .01
        return interest
        
        
        """calculate and return interest gained on account"""
    def print_history(self):
        for i in self.history:
            print(i)
            return self.history 
        
        
             
      

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
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'history':
        history = atm.print_history()
        print(f'Your transaction history is {history}')
        
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
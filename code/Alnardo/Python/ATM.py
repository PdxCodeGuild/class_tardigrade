class ATM:
    def __init__(self, balance=0, interest_rate=0.001):
        # self.transaction = transaction
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    # transactions = []

    def check_balance(self):
        """return the account balance"""
        return self.balance

    def deposit(self, amount):
        """deposit a given amount into account"""
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')

        return self.balance

    def check_withdrawal(self, amount):
        """return True if account has enough funds to withdraw given amount"""
        balance = self.balance - amount
        if balance >= 0.0:
            return True
        else:
            return False

    def withdraw(self, amount):
        """withdraw given amount from account and return that amount"""
        self.balance -= amount
        self.transactions.append(f'User withdrew ${amount}')

        return self.balance
        

    def calc_interest(self):
        """calculate and return interest gained on account"""
        bonus_money = self.balance * self.interest_rate
        # bonus_money += self.balance
        return bonus_money

    def print_transaction(self):
        """print total transactions"""
        # if command == 'deposit':
        #     transactions.append(f'Deposited ${amount}')
        # elif command == 'withdraw':
        #     transactions.append(f'Withdrew ${amount}')
        return print(self.transactions)






# transactions = []

atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit?: '))
        atm.deposit(amount)  # call the deposit(amount) method
        # print(f'Deposited ${amount}')
        # transactions.append(f'User deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like: '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            # print(f'Withdrew ${amount}')
            # transactions.append(f'User withdrew ${amount}')
        else:
            print('Insufficient funds')
            # transactions.append('Attempted to overdraw account.')
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest!')
    elif command == 'print':
        atm.print_transaction()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('print    - print transactions')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
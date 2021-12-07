class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        for self in self:
            print(self)

        
    # def deposit(self, amount):
    #     """deposit a given amount into account"""
    #     ...

    # def check_withdrawal(self, amount):
    #     """return True if account has enough funds to withdraw given amount"""
    #     ...

    # def withdraw(self, amount):
    #     """withdraw given amount from account and return that amount"""
    #     ...

    # def calc_interest(self):
    #     """calculate and return interest gained on account"""
    #     ...

# The "Draw a square" demo is meant to explain how the computer interprets your code. (edited)

# # version 2
# # have the ATM maintain a list of transactions

# # version 3
# # allow the user to enter commands
# # e.g. 'what would you like to do? (deposit, withdraw, check balance)'

# # ATM class containing two attributes: a balance and an interest rate
# # newly created accounts have a balance of 0 and an interest rate of 0.1%
# # check_balance() returns the account balance
# # deposit(amount) deposits the given amount in the account
# # check_withdrawal(amount) returns true if withdrawn amount won't put account in the negative
# # withdraw(amount) withdraws the amount from the account and returns it
# # calc_interest() returns the amount of interest calculated on the account

class Atm:
    def __init__(self, balance=0, interest_rate=0.1):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        print('your balance is: ' + str(self.balance))
        print('your interest rate is: ' + str(self.interest_rate))

    def deposit(self, amount):
        self.balance += amount
        print('your new balance is: ' + str(self.balance))

    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        print('please remove your cash ($' + str(amount) + ')')
        print('your new balance is: ' + str(self.balance))

    def calc_interest(self):
        print('your interest is: ' + str(self.balance * self.interest_rate))

def withdraw(amount):

    if atm1.check_withdrawal(int(amount)):
        atm1.withdraw(amount)
    else:
        try_again = input('amount unavailable, enter another amount or c to cancel 1 ')
        if try_again == 'c':
            print('goodbye')
        elif try_again.isalpha():
            withdraw(amount = int(input('enter a withdrawal amount: ')))
            # try_again = input('please enter another amount or c to cancel 2 ') #add recursion
            # withdraw(int(try_again))
        else:
            withdraw(int(try_again))

atm1 = Atm(0, 0.1)
atm1.check_balance()
deposit_amount = int(input('enter a deposit amount: '))
atm1.deposit(deposit_amount)
withdraw(amount = int(input('enter a withdrawal amount: ')))


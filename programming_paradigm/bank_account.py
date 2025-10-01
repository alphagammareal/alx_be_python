# Create a simple bank account class

class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    # Deposit
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    # Withdraw
    def withdraw(self, amount):
        if amount <= self.account_balance:
            print(True)
            self.account_balance -= amount
            return self.account_balance
        elif amount > self.account_balance:
            print(False)
            return self.account_balance

    # display Balnce
    def display_balance(self):
         print(f"Current balance: ${self.account_balance:.2f}")
    